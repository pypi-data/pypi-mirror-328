import redis
import time
import json
import uuid
from functools import wraps
from typing import Optional, Dict, Callable, Any
from concurrent.futures import ThreadPoolExecutor
import threading


class QueueWorker:
    """
    A worker that processes tasks from a Redis stream.

    Attributes
    ----------
    TASK_REGISTRY : dict
        A dictionary to store registered tasks.

    Methods
    -------
    task(name)
        Decorator to register a task function.
    run(max_thread=1000, block=None, count=None)
        Continuously reads task messages from the Redis stream and executes registered tasks.
    _process_message(message_id, message)
        Processes a single message and executes the corresponding task.
        
    Example
    -------
    ```python
    from edalite.queue import QueueWorker

    worker = QueueWorker(
        redis_url="redis://localhost:6379/0",
        queue_stream_name="edalite_queue",
        queue_group_name="worker",
        request_result_stream_name="edalite_request_result",
        consumer_name="worker_1",
        debug=True,
    )
    
    @worker.task("example_task")
    def handle(data):
        print(f"Executing example_task: {data}")
        return f"Completed example_task: {data}"

    worker.run(max_thread=10, block=1000, count=10)
    ```
    """

    TASK_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        queue_stream_name: str = "edalite_queue",
        queue_group_name: str = "worker",
        request_result_stream_name: str = "edalite_request_result",
        consumer_name: Optional[str] = None,
        debug: bool = False,
    ) -> None:
        """
        Initializes the QueueWorker with Redis connection and consumer group.

        Parameters
        ----------
        redis_url : str, optional
            The URL for the Redis server (default is "redis://localhost:6379/0").
        queue_stream_name : str, optional
            The name of the Redis stream for the queue (default is "edalite_queue").
        queue_group_name : str, optional
            The name of the consumer group (default is "worker").
        request_result_stream_name : str, optional
            The name of the stream for request results (default is "edalite_request_result").
        consumer_name : str, optional
            The name of the consumer (default is None, which generates a unique name).
        debug : bool, optional
            If True, enables debug mode with additional logging (default is False).

        Example
        -------
        ```python
        worker = QueueWorker(
            redis_url="redis://localhost:6379/0",
            queue_stream_name="my_queue",
            queue_group_name="my_group",
            request_result_stream_name="my_result_stream",
            consumer_name="my_consumer",
            debug=True
        )
        ```
        """
        self.redis = redis.Redis.from_url(redis_url)
        self.queue_stream_name = queue_stream_name
        self.queue_group_name = queue_group_name
        self.request_result_stream_name = request_result_stream_name
        self.debug = debug

        if consumer_name is None:
            consumer_name = f"worker-{uuid.uuid4().hex}"
        self.consumer_name = consumer_name

        try:
            self.redis.xgroup_create(
                name=self.queue_stream_name,
                groupname=self.queue_group_name,
                id="0",
                mkstream=True,
            )
        except redis.exceptions.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise

    @classmethod
    def task(cls, name: str) -> Callable[[Callable[[Dict[str, Any]], Any]], Callable[[Dict[str, Any]], Any]]:
        """
        Decorator to register a task function.

        Parameters
        ----------
        name : str
            The name of the task to register.

        Returns
        -------
        function
            The wrapped function that registers the task.

        Example
        -------
        ```python
        @QueueWorker.task("my_task")
        def my_task_function(data):
            print(f"Processing data: {data}")
            return "Task completed"
        ```
        """
        def decorator(func: Callable[[Dict[str, Any]], Any]) -> Callable[[Dict[str, Any]], Any]:
            cls.TASK_REGISTRY[name] = func

            @wraps(func)
            def wrapper(data: Dict[str, Any]) -> Any:
                return func(data)

            return wrapper
        return decorator

    def run(self, max_thread: int = 1000, block: Optional[int] = None, count: Optional[int] = None) -> None:
        """
        Continuously reads task messages from the Redis stream and executes registered tasks.

        Parameters
        ----------
        max_thread : int, optional
            Maximum number of threads (default is 1000).
        block : int, optional
            Blocking wait time for xreadgroup in milliseconds (default is None).
        count : int, optional
            Maximum number of messages to read at once (default is None).

        Example
        -------
        ```python
        worker.run(max_thread=5)
        ```
        """
        executor = (
            ThreadPoolExecutor(max_workers=max_thread) if max_thread > 1 else None
        )
        
        print(f"QueueWorker started - Max threads: {max_thread}")
        print(f"QueueWorker started - Stream name: {self.queue_stream_name}")
        print(f"QueueWorker started - Group name: {self.queue_group_name}")
        print(f"QueueWorker started - Request result stream name: {self.request_result_stream_name}")
        print(f"QueueWorker started - Consumer name: {self.consumer_name}")
        print(f"QueueWorker started - Registered tasks count: {len(self.TASK_REGISTRY)}")
        
        if self.debug:
            print(f"QueueWorker started - Registered tasks: {self.TASK_REGISTRY.keys()}")

        while True:
            try:
                messages = self.redis.xreadgroup(
                    groupname=self.queue_group_name,
                    consumername=self.consumer_name,
                    streams={self.queue_stream_name: ">"},
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
                if self.debug:
                    print(f"Error reading stream: {e}")
                time.sleep(1)

    def _process_message(self, message_id: str, message: Dict[bytes, bytes]) -> None:
        """
        Processes a single message and executes the corresponding task.

        Parameters
        ----------
        message_id : str
            The ID of the message in the Redis stream.
        message : dict
            The message data containing task information.

        Example
        -------
        This method is used internally and is not typically called directly.
        """
        current_thread = threading.current_thread().name
        if self.debug:
            print(f"Current thread: {current_thread}")

        task_type = None
        result_payload = None

        try:
            task_info = json.loads(next(iter(message.values())).decode())
            task_name = task_info.get("task_name")
            data = task_info.get("data")
            task_type = task_info.get("type")

            if not task_type:
                raise ValueError("Task type is not specified")

            if task_name in self.TASK_REGISTRY:
                self.redis.set(f"{self.queue_stream_name}:{message_id}", json.dumps({"status": "PROCESSING", "result": None}))
                
                func = self.TASK_REGISTRY[task_name]
                if self.debug:
                    print(f"Executing task: {task_name} / data: {data}")

                result = func(data)
                result_payload = json.dumps({"status": "COMPLETED", "result": result})
            else:
                if self.debug:
                    print(f"Unregistered task: {task_name}")
                result_payload = json.dumps(
                    {"status": "FAILURE", "error": "Unregistered task", "result": None}
                )
                
        except Exception as ex:
            if self.debug:
                print(f"Error processing task: {ex}")
            result_payload = json.dumps({"status": "FAILURE", "error": str(ex), "result": None})
            
        finally:
            if result_payload:
                if task_type == "delay":
                    self.redis.set(f"{self.queue_stream_name}:{message_id}", result_payload)

                if task_type == "request":
                    self.redis.xadd(
                        self.request_result_stream_name,
                        {"task_id": message_id, "result": result_payload},
                    )
                    
                self.redis.xack(self.queue_stream_name, self.queue_group_name, message_id)


class QueueCaller:
    """
    A caller that sends tasks to a Redis stream and retrieves results.

    Methods
    -------
    delay(task_name, data, decode=True)
        Sends a 'delay' type task and stores the result asynchronously.
    request(task_name, data, timeout=30, block=None, count=None)
        Sends a 'request' type task and waits for the result synchronously.
    get_result(task_id)
        Retrieves the result for a given task_id from Redis.
    """

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        queue_stream_name: str = "edalite_queue",
        request_result_stream_name: str = "edalite_request_result",
    ) -> None:
        """
        Initializes the QueueCaller with Redis connection.

        Parameters
        ----------
        redis_url : str, optional
            The URL for the Redis server (default is "redis://localhost:6379/0").
        queue_stream_name : str, optional
            The name of the Redis stream for the queue (default is "edalite_queue").
        request_result_stream_name : str, optional
            The name of the stream for request results (default is "edalite_request_result").

        Example
        -------
        ```python
        caller = QueueCaller(
            redis_url="redis://localhost:6379/0",
            queue_stream_name="my_queue",
            request_result_stream_name="my_result_stream"
        )
        ```
        """
        self.redis = redis.Redis.from_url(redis_url)
        self.queue_stream_name = queue_stream_name
        self.request_result_stream_name = request_result_stream_name

    def delay(self, task_name: str, data: Dict[str, Any], decode: bool = True) -> str:
        """
        Sends a 'delay' type task and stores the result asynchronously.

        Parameters
        ----------
        task_name : str
            The name of the task to execute.
        data : dict
            The data to pass to the task.
        decode : bool, optional
            If True, decodes the task ID to a string (default is True).

        Returns
        -------
        str
            The task ID.

        Example
        -------
        ```python
        task_id = caller.delay("my_task", {"key": "value"})
        print(f"Task ID: {task_id}")
        ```
        """
        task_data = json.dumps({"task_name": task_name, "data": data, "type": "delay"})
        
        task_id = self.redis.xadd(self.queue_stream_name, {"data": task_data})
        
        self.redis.set(f"{self.queue_stream_name}:{task_id}", json.dumps({"status": "QUEUED", "result": None}))

        return task_id.decode() if decode else task_id

    def request(self, task_name: str, data: Dict[str, Any], timeout: int = 30, block: Optional[int] = None, count: Optional[int] = None) -> Dict[str, Any]:
        """
        Sends a 'request' type task and waits for the result synchronously.

        Parameters
        ----------
        task_name : str
            The name of the task to execute.
        data : dict
            The data to pass to the task.
        timeout : int, optional
            The total timeout for the task in seconds (default is 30).
        block : int, optional
            Blocking wait time for Redis stream read in milliseconds (default is None).
        count : int, optional
            Maximum number of messages to read at once (default is None).

        Returns
        -------
        dict
            The result of the task.

        Raises
        ------
        TimeoutError
            If the task does not complete within the specified timeout.

        Example
        -------
        ```python
        try:
            result = caller.request("my_task", {"key": "value"}, timeout=10)
            print(f"Task result: {result}")
        except TimeoutError as e:
            print(f"Task timed out: {e}")
        ```
        """
        task_data = json.dumps(
            {"task_name": task_name, "data": data, "type": "request"}
        )
        
        task_id = self.redis.xadd(self.queue_stream_name, {"data": task_data})

        last_id = "0"
        start_time = time.time()

        while True:
            try:
                if timeout and (time.time() - start_time) > timeout:
                    raise TimeoutError(
                        f"Task {task_name} did not complete within {timeout} seconds"
                    )
                
                messages = self.redis.xread(
                    {self.request_result_stream_name: last_id}, block=block, count=count
                )

                if messages:
                    for stream, msgs in messages:
                        for msg_id, fields in msgs:
                            last_id = msg_id
                            if fields[b"task_id"] == task_id:
                                self.redis.xdel(self.request_result_stream_name, msg_id)
                                return json.loads(fields[b"result"].decode())
                            
            except Exception as e:
                print(f"Error: {e}")
                self.redis.xdel(self.queue_stream_name, task_id)

    def get_result(self, task_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the result for a given task_id from Redis.

        Parameters
        ----------
        task_id : str
            The ID of the task to retrieve the result for.

        Returns
        -------
        dict or None
            The parsed JSON result if available, otherwise None.

        Example
        -------
        ```python
        result = caller.get_result(task_id)
        if result:
            print(f"Task result: {result}")
        else:
            print("No result found for the task.")
        ```
        """
        result = self.redis.get(f"{self.queue_stream_name}:{task_id.encode()}")
        if result:
            return json.loads(result.decode())
        return None
