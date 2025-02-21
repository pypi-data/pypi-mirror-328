#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis 기반 Edalite Worker 및 Caller 구현
===========================================

이 모듈은 Redis의 Pub/Sub와 KV 스토어를 이용하여 즉시 실행(immediate)과 지연 실행(deferred)을
동기 방식으로 지원합니다.

작업 요청은 Redis 채널("tasks:{subject}")를 통해 전달되며,
즉시 작업 요청은 reply_channel 정보를 포함하여, 작업 수행 후 해당 채널에 결과를 발행(publish)합니다.
지연 작업 요청은 caller가 미리 생성한 task_id를 기준으로, 작업 상태(QUEUED, PROCESSING, COMPLETED, FAILURE)를
Redis KV 스토어에 기록합니다.

Classes
-------
EdaliteWorker
    등록된 작업을 Redis 채널을 통해 수신하며, 동기 방식으로 작업을 즉시 실행하거나 지연 실행합니다.
EdaliteCaller
    Redis 채널에 작업 요청을 발행하며, 즉시 작업의 경우 응답 채널을 통해 결과를 수신하고, 지연 작업은 task_id를 발행합니다.
"""

import json
import uuid
import time
import threading
import concurrent.futures
from typing import Callable, Any, Union, List
import os

from redis import Redis


##############################################################################
# Synchronous Worker Implementation using Redis (Pub/Sub and KV Storage)
##############################################################################
class EdaliteWorker:
    """
    Redis 기반 동기 worker.
    
    - 클라이언트는 작업 요청 시 JSON 페이로드에 "mode" 필드("immediate" 또는 "deferred")와
      "data" 항목을 포함하여, 채널 "tasks:{subject}"에 메시지를 발행합니다.
    - 즉시 작업의 경우, 추가로 "reply_channel" 필드를 포함하여 응답받을 임시 채널을 명시합니다.
    - 지연 작업의 경우, 미리 생성된 task_id가 포함되며 caller가 Redis에 초기(QUEUED) 상태를 저장합니다.
    
    작업 실행 후 결과는 다음과 같이 처리됩니다:
      - 즉시: reply_channel을 통해 결과가 전송됨.
      - 지연: Redis에 상태를 업데이트 (PROCESSING → COMPLETED/FAILURE).
    """

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        debug: bool = False,
        max_thread: int = 1,
    ):
        self.redis_url = redis_url
        self.debug = debug
        self.max_thread = max_thread

        # 작업 등록: subject -> list of (function, queue_group)
        self.tasks = {}

        # Redis 연결 (명령과 Pub/Sub용 별도 연결)
        self._redis = Redis.from_url(self.redis_url, decode_responses=True)
        self._pubsub = None

        # 최대 스레드 수에 따른 쓰레드 풀 (max_thread가 1이면 동기 실행)
        self.task_executor = (
            concurrent.futures.ThreadPoolExecutor(max_workers=self.max_thread)
            if self.max_thread > 1
            else None
        )

    def task(self, subject: str, queue_group: str = None) -> Callable:
        """
        주어진 subject에 대한 작업 함수를 등록합니다.
        
        Parameters:
            subject (str): 작업 채널 이름에 사용할 주제.
            queue_group (str, optional): 동일 subject 내 중복 등록 방지용 (사용 시 한 개만 허용).
        
        Returns:
            Callable: 장식된 함수.
        """
        def decorator(func: Callable):
            if subject not in self.tasks:
                self.tasks[subject] = []
            for _, existing_queue in self.tasks[subject]:
                if existing_queue == queue_group:
                    raise ValueError(
                        f"Queue group '{queue_group}' is already registered for subject '{subject}'"
                    )
            self.tasks[subject].append((func, queue_group))
            if self.debug:
                print(f"[Worker] Registered task for subject '{subject}'")
            return func
        return decorator

    def start(self):
        """
        등록된 모든 subject의 Redis 채널("tasks:{subject}")에 구독하여 작업을 처리합니다.
        
        이 메서드는 블로킹되며, Ctrl+C로 종료할 수 있습니다.
        """
        # 구독용 Redis 클라이언트 생성 (Pub/Sub 전용)
        self._pubsub = self._redis.pubsub(ignore_subscribe_messages=True)
        channels = ["tasks:" + subject for subject in self.tasks.keys()]
        if channels:
            self._pubsub.subscribe(*channels)
            if self.debug:
                print("[Worker] 구독중인 채널:", channels)
        else:
            if self.debug:
                print("[Worker] 등록된 subject가 없습니다.")
            return

        try:
            if self.debug:
                print(f"[Worker] 시작 (PID: {os.getpid()})")
            while True:
                message = self._pubsub.get_message()
                if message:
                    self._handle_message(message)
                time.sleep(0.01)
        except KeyboardInterrupt:
            if self.debug:
                print(f"[Worker] 종료 중... (PID: {os.getpid()})")
            self._pubsub.close()
            if self.task_executor:
                self.task_executor.shutdown(wait=False)

    def _handle_message(self, message: dict):
        """
        Redis Pub/Sub 메시지를 처리합니다.
        메시지 채널 이름은 "tasks:{subject}" 형식을 가지며, JSON 페이로드는 다음 필드를 포함합니다:
          - mode: "immediate" 또는 "deferred"
          - data: 작업 입력 데이터
          - (immediate의 경우) reply_channel: 응답을 받을 채널
          - (deferred의 경우) task_id: caller가 미리 생성한 작업 ID
        """
        try:
            payload = json.loads(message["data"])
        except Exception as e:
            if self.debug:
                print(f"[Worker] payload 파싱 오류: {e}")
            return

        mode = payload.get("mode", "immediate")
        data = payload.get("data")
        # 채널 이름에서 subject 추출 ("tasks:{subject}" → subject)
        channel = message.get("channel", "")
        subject = channel.split("tasks:", 1)[-1]
        if data is None:
            if self.debug:
                print(f"[Worker] '{subject}' 채널: 'data' 항목 누락")
            return

        # subject에 등록된 작업 핸들러(들) 중 첫 번째 핸들러 선택
        if subject not in self.tasks or not self.tasks[subject]:
            if self.debug:
                print(f"[Worker] subject '{subject}'에 등록된 작업이 없음.")
            return
        task, _ = self.tasks[subject][0]

        if mode == "immediate":
            reply_channel = payload.get("reply_channel")
            if not reply_channel:
                if self.debug:
                    print(f"[Worker] 즉시 작업: '{subject}' 채널, reply_channel 없음")
                return
            if self.debug:
                print(f"[Worker] 즉시 작업 수신, subject='{subject}', data={data}, reply_channel={reply_channel}")
            if self.task_executor:
                future = self.task_executor.submit(self._execute_task, task, data)
                future.add_done_callback(lambda f: self._respond_immediate(reply_channel, f))
            else:
                try:
                    result = self._execute_task(task, data)
                    if self.debug:
                        print(f"[Worker] 즉시 작업 결과: {result}")
                    self._redis.publish(reply_channel, str(result))
                except Exception as e:
                    if self.debug:
                        print(f"[Worker] 즉시 작업 오류: {e}")
                    self._redis.publish(reply_channel, f"Error: {str(e)}")
        elif mode == "deferred":
            task_id = payload.get("task_id")
            if not task_id:
                if self.debug:
                    print(f"[Worker] 지연 작업: '{subject}' 채널, task_id 누락")
                return
            if self.debug:
                print(f"[Worker] 지연 작업 수신, subject='{subject}', data={data}, task_id={task_id}")
            # 작업 상태를 PROCESSING으로 업데이트
            self._publish_deferred_status(subject, task_id, "PROCESSING", None)
            if self.task_executor:
                future = self.task_executor.submit(self._execute_task, task, data)
                future.add_done_callback(lambda f: self._handle_deferred(subject, task_id, f))
            else:
                try:
                    result = self._execute_task(task, data)
                    self._publish_deferred_status(subject, task_id, "COMPLETED", result)
                except Exception as e:
                    self._publish_deferred_status(subject, task_id, "FAILURE", str(e))
        else:
            if self.debug:
                print(f"[Worker] 알 수 없는 mode '{mode}'")

    @staticmethod
    def _execute_task(task: Callable, data: Any):
        """작업 함수를 실행합니다."""
        return task(data)

    def _respond_immediate(self, reply_channel: str, future: concurrent.futures.Future):
        """즉시 작업 실행 후 reply_channel로 결과를 발행합니다."""
        try:
            result = future.result()
            if self.debug:
                print(f"[Worker] 즉시 작업 결과 전송: {result}")
            self._redis.publish(reply_channel, str(result))
        except Exception as e:
            if self.debug:
                print(f"[Worker] 즉시 작업 오류 전송: {e}")
            self._redis.publish(reply_channel, f"Error: {str(e)}")

    def _handle_deferred(self, subject: str, task_id: str, future: concurrent.futures.Future):
        """지연 작업 실행 후 Redis KV에 작업 상태 및 결과를 업데이트합니다."""
        try:
            result = future.result()
            self._publish_deferred_status(subject, task_id, "COMPLETED", result)
            if self.debug:
                print(f"[Worker] 지연 작업 완료, task_id={task_id}, 결과: {result}")
        except Exception as e:
            self._publish_deferred_status(subject, task_id, "FAILURE", str(e))
            if self.debug:
                print(f"[Worker] 지연 작업 실패, task_id={task_id}, 오류: {e}")

    def _publish_deferred_status(self, subject: str, task_id: str, status: str, result: Any):
        """
        지연 작업의 상태와 결과를 Redis KV에 기록합니다.
        키 형식: DEFERRED_TASKS_{subject.replace('.', '_')}:{task_id}
        """
        redis_key = f"DEFERRED_TASKS_{subject.replace('.', '_')}:{task_id}"
        doc = {"task_id": task_id, "status": status, "result": result}
        try:
            self._redis.set(redis_key, json.dumps(doc))
        except Exception as e:
            if self.debug:
                print(f"[Worker][Redis] 작업 상태 저장 오류 {redis_key}: {e}")


##############################################################################
# Synchronous Caller Implementation using Redis (Pub/Sub and KV Storage)
##############################################################################
class EdaliteCaller:
    """
    Redis 기반 동기 caller.
    
    - 즉시 작업 호출(request): "tasks:{subject}" 채널에 메시지를 발행하고, reply_channel을 통해 결과를 수신합니다.
    - 지연 작업 호출(delay): caller가 미리 task_id를 생성하고, 초기 상태를 Redis에 기록한 후 메시지를 발행합니다.
      이후 작업 결과는 Redis KV에서 확인할 수 있습니다.
    """

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        debug: bool = False,
    ):
        self.redis_url = redis_url
        self.debug = debug
        self._redis = Redis.from_url(self.redis_url, decode_responses=True)

    def request(self, subject: str, data: Any, timeout: float = 30.0) -> str:
        """
        즉시 실행 작업을 호출하고 결과를 반환합니다.
        
        메시지 페이로드: {"mode": "immediate", "data": <data>, "reply_channel": <임시 채널>}
        """
        reply_channel = "reply:" + uuid.uuid4().hex
        payload = json.dumps({
            "mode": "immediate",
            "data": str(data),
            "reply_channel": reply_channel
        })
        # 응답을 받기 위한 전용 Pub/Sub 구독
        pubsub = self._redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(reply_channel)
        # 작업 요청 메시지 발행
        self._redis.publish("tasks:" + subject, payload)
        if self.debug:
            print(f"[Caller] 즉시 작업 요청, subject='{subject}', reply_channel={reply_channel}")

        # 응답 대기 (timeout까지 폴링)
        start_time = time.time()
        response = None
        while time.time() - start_time < timeout:
            message = pubsub.get_message()
            if message and message.get("type") == "message":
                response = message.get("data")
                break
            time.sleep(0.01)
        pubsub.unsubscribe(reply_channel)
        pubsub.close()

        if response is None:
            raise TimeoutError(f"즉시 작업 응답 대기 시간 초과 (subject: {subject})")
        if isinstance(response, bytes):
            response = response.decode()
        if response.startswith("Error:"):
            raise RuntimeError(response[6:].strip())
        return response

    def delay(self, subject: str, data: Any, timeout: float = 30.0) -> str:
        """
        지연 실행 작업을 호출합니다.
        
        메시지 페이로드: {"mode": "deferred", "data": <data>, "task_id": <생성된 ID>}
        caller는 미리 Redis에 초기 상태(QUEUED)를 기록합니다.
        """
        task_id = str(uuid.uuid4())
        redis_key = f"DEFERRED_TASKS_{subject.replace('.', '_')}:{task_id}"
        doc = {"task_id": task_id, "status": "QUEUED", "result": None}
        try:
            self._redis.set(redis_key, json.dumps(doc))
        except Exception as e:
            if self.debug:
                print(f"[Caller][Redis] 초기 작업 상태 저장 오류: {e}")
        payload = json.dumps({
            "mode": "deferred",
            "data": str(data),
            "task_id": task_id
        })
        self._redis.publish("tasks:" + subject, payload)
        if self.debug:
            print(f"[Caller] 지연 작업 요청, subject='{subject}', task_id={task_id}")
        return task_id

    def get_deferred_result(self, subject: str, task_id: str) -> dict:
        """
        Redis KV에서 지연 작업의 결과와 상태를 조회합니다.
        키 형식: DEFERRED_TASKS_{subject.replace('.', '_')}:{task_id}
        """
        redis_key = f"DEFERRED_TASKS_{subject.replace('.', '_')}:{task_id}"
        try:
            value = self._redis.get(redis_key)
            if value is None:
                return {"error": f"task_id={task_id}에 해당하는 데이터가 없습니다."}
            data = json.loads(value)
            return data
        except Exception as e:
            return {"error": str(e)}

    def close(self):
        """
        caller의 Redis 연결을 종료합니다.
        """
        try:
            self._redis.close()
        except Exception:
            pass
