import redis
import time
import json
import uuid
from functools import wraps
from typing import Optional
from concurrent.futures import ThreadPoolExecutor
import threading


class EdaliteWorker:
    # 등록된 작업을 저장할 딕셔너리
    TASK_REGISTRY = {}

    def __init__(
        self,
        redis_url="redis://localhost:6379/0",
        task_stream_name="edalite_task",
        task_group_name="group1",
        result_stream_name="edalite_result",
        result_key_prefix="edalite_result",
        consumer_name=None,
    ):
        """

        Redis 연결 설정 및 소비자 그룹을 생성합니다.
        """
        self.redis = redis.Redis.from_url(redis_url)
        self.task_stream_name = task_stream_name
        self.task_group_name = task_group_name
        self.result_stream_name = result_stream_name
        self.result_key_prefix = result_key_prefix

        if consumer_name is None:
            consumer_name = f"worker-{uuid.uuid4().hex}"
        self.consumer_name = consumer_name

        # consumer group이 없으면 새로 생성 (mkstream=True를 통해 스트림이 없을 경우 자동 생성)
        try:
            self.redis.xgroup_create(
                name=self.task_stream_name,
                groupname=self.task_group_name,
                id="0",
                mkstream=True,
            )
        except redis.exceptions.ResponseError as e:

            if "BUSYGROUP" not in str(e):
                raise

    @classmethod
    def task(cls, func):
        """
        작업 함수를 등록하는 데코레이터.
        함수 이름을 키로 하여 작업을 저장합니다.
        """
        cls.TASK_REGISTRY[func.__name__] = func

        @wraps(func)
        def wrapper(data: dict):
            return func(data)

        return wrapper

    def run(self, block: Optional[int] = 1000, count: int = 1, max_thread: int = 1):
        """
        Redis 스트림에서 작업 메시지를 계속 읽어와 등록된 작업을 실행합니다.
        block: xreadgroup의 블록 대기시간 (밀리초)
        max_thread: 최대 스레드 수 (1이면 순차적으로 실행, 1보다 크면 멀티쓰레드로 실행)
        """
        # max_thread가 1보다 크면 ThreadPoolExecutor를 사용하여 멀티쓰레드 처리
        executor = (
            ThreadPoolExecutor(max_workers=max_thread) if max_thread > 1 else None
        )

        while True:
            try:
                messages = self.redis.xreadgroup(
                    groupname=self.task_group_name,
                    consumername=self.consumer_name,
                    streams={self.task_stream_name: ">"},
                    count=count,
                    block=block,
                )

                if not messages:
                    continue

                for stream, msgs in messages:
                    for message_id, message in msgs:
                        if executor:
                            executor.submit(self._process_message, message_id, message)
                        else:
                            self._process_message(message_id, message)
            except Exception as e:
                print(f"스트림 읽기 중 에러 발생: {e}")
                time.sleep(1)

    def _process_message(self, message_id, message):
        """
        단일 메시지에 대한 작업 실행 처리
        """
        # 현재 스레드 이름 출력
        current_thread = threading.current_thread().name
        print(f"현재 스레드: {current_thread}")

        task_type = None
        result_payload = None

        try:
            # 메시지의 값은 딕셔너리 형태의 단일 키-값 쌍으로 구성되어 있음
            task_info = json.loads(next(iter(message.values())).decode())
            task_name = task_info.get("task_name")
            data = task_info.get("data")
            task_type = task_info.get("type")

            if not task_type:
                raise ValueError("작업 타입이 지정되지 않았습니다")

            if task_name in self.TASK_REGISTRY:
                func = self.TASK_REGISTRY[task_name]
                print(f"작업 실행: {task_name} / data: {data}")

                # 함수 실행 후 결과 저장
                result = func(data)
                print(result)
                result_payload = json.dumps({"status": "success", "result": result})
            else:
                print(f"등록되지 않은 작업: {task_name}")
                result_payload = json.dumps(
                    {"status": "error", "error": "등록되지 않은 작업"}
                )
        except Exception as ex:
            print(f"작업 처리 중 에러 발생: {ex}")
            result_payload = json.dumps({"status": "error", "error": str(ex)})
        finally:
            if result_payload:
                # 작업 결과를 Redis KV에 저장 (두 요청 모두)
                self.redis.set(f"{self.result_key_prefix}:{message_id}", result_payload)
                # 요청 타입에 따라 edalite_results 스트림 사용 여부 결정

                if task_type == "request":
                    self.redis.xadd(
                        self.result_stream_name,
                        {"task_id": message_id, "result": result_payload},
                    )
                self.redis.xack(self.task_stream_name, self.task_group_name, message_id)


class EdaliteCaller:
    def __init__(
        self,
        redis_url="redis://localhost:6379/0",
        task_stream_name="edalite_task",
        result_stream_name="edalite_result",
        result_key_prefix="edalite_result",
    ):
        """
        Redis 연결을 설정합니다.

        """
        self.redis = redis.Redis.from_url(redis_url)
        self.task_stream_name = task_stream_name
        self.result_stream_name = result_stream_name
        self.result_key_prefix = result_key_prefix

    def delay(self, task_name, data, decode=True):
        """
        delay 작업: 'delay' 타입으로 작업을 보내고 비동기적으로 결과를 저장합니다.
        워커는 결과를 Redis KV에 저장하며, edalite_results 스트림은 사용하지 않습니다.
        """
        task_data = json.dumps({"task_name": task_name, "data": data, "type": "delay"})
        
        custom_id = uuid.uuid4().hex
        task_id = self.redis.xadd(self.task_stream_name, {"data": task_data}, id=custom_id)
        return task_id.decode() if decode else task_id

    def request(self, task_name, data, timeout=30, block=None, count=None):
        """
        request 작업: 'request' 타입으로 작업을 보내고, edalite_results 스트림을 통해
        결과를 동기적으로 기다립니다.

        매개변수:
            task_name: 실행할 작업의 이름
            data: 작업에 전달할 데이터
            timeout: 전체 작업 타임아웃 (초). None이면 무한 대기
            block: Redis 스트림 읽기 대기 시간 (밀리초)
            count: 한 번에 읽을 최대 메시지 수
        """
        task_data = json.dumps(
            {"task_name": task_name, "data": data, "type": "request"}
        )
        task_id = self.redis.xadd(self.task_stream_name, {"data": task_data})

        last_id = "0"
        start_time = time.time()

        while True:
            if timeout and (time.time() - start_time) > timeout:
                raise TimeoutError(
                    f"작업 {task_name}이(가) {timeout}초 내에 완료되지 않았습니다"
                )

            messages = self.redis.xread(
                {self.result_stream_name: last_id}, block=block, count=count
            )

            if messages:
                for stream, msgs in messages:
                    for msg_id, fields in msgs:
                        last_id = msg_id
                        if fields[b"task_id"] == task_id:
                            self.redis.xdel(self.result_stream_name, msg_id)
                            return json.loads(fields[b"result"].decode())

    def get_result(self, task_id):
        """
        주어진 task_id에 대한 결과를 Redis에서 가져옵니다.
        결과가 있으면 JSON 형태로 파싱한 값을 반환하고, 없으면 None을 반환합니다.
        """
        result = self.redis.get(f"{self.result_key_prefix}:{task_id.encode()}")
        if result:
            return json.loads(result.decode())
        return None
