import redis
import json
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import threading
from typing import Optional, Dict, Callable, Any

class PubSubWorker:
    """
    A worker that processes tasks from a Redis Pub/Sub channel.

    Attributes
    ----------
    TASK_REGISTRY : dict
        A dictionary to store registered tasks.

    Methods
    -------
    task(name)
        Decorator to register a task function.
    run(max_thread=1000, timeout=0)
        Subscribes to the Redis Pub/Sub channel and processes messages.
    _process_message(name, data)
        Processes a single message and executes the corresponding task.
        
    Examples
    --------
    ```python
    from edalite.pubsub import PubSubWorker

    worker = PubSubWorker(redis_url="redis://localhost:6379/0", channel="edalite_pubsub", debug=True)
    
    @worker.task("my_task")
    def my_task_function(data):
        print(f"Processing data: {data}")
        return "Task completed"

    worker.run(max_thread=5)
    ```
    """

    TASK_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    def __init__(self, redis_url: str = "redis://localhost:6379/0", channel: str = "edalite_pubsub", debug: bool = False) -> None:
        """
        Initializes the PubSubWorker with Redis connection and channel name.

        Parameters
        ----------
        redis_url : str, optional
            The URL for the Redis server (default is "redis://localhost:6379/0").
        channel : str, optional
            The name of the Redis Pub/Sub channel (default is "edalite_pubsub").
        debug : bool, optional
            If True, enables debug mode with additional logging (default is False).

        Example
        -------
        ```python
        worker = PubSubWorker(redis_url="redis://localhost:6379/0", channel="my_channel", debug=True)
        ```
        """
        self.redis = redis.Redis.from_url(redis_url)
        self.channel = channel
        self.debug = debug
        
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
        @PubSubWorker.task("example_task")
        def example_task_function(data):
            print(f"Executing example_task: {data}")
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

    def run(self, max_thread: int = 1000, timeout: Optional[float] = 0) -> None:
        """
        Subscribes to the Redis Pub/Sub channel and processes messages.

        Parameters
        ----------
        max_thread : int, optional
            Maximum number of threads (default is 1000).
        timeout : float, optional
            Blocking wait time for getting messages from the Pub/Sub channel (default is 0).

        Example
        -------
        ```python
        worker.run(max_thread=10)
        ```
        """
        executor = ThreadPoolExecutor(max_workers=max_thread) if max_thread else None
        pubsub = self.redis.pubsub()

        # Subscribe to all task names in TASK_REGISTRY
        pubsub.subscribe(self.channel)
        
        print(f"PubSubWorker started - Max threads: {max_thread}")
        print(f"PubSubWorker started - Subscribed channel count: {len(self.TASK_REGISTRY)}")
            
        if self.debug:
            print(f"Subscribed channels: {self.TASK_REGISTRY.keys()}")

        try:
            while True:
                message = pubsub.get_message(timeout=timeout)
                if message:
                    if self.debug:
                        print(f"PubSubWorker received message: {message}")
                    if message['type'] == 'message':
                        task_data = json.loads(message['data'].decode())
                        
                        name = task_data.get("name")
                        data = task_data.get("data")

                        if name in self.TASK_REGISTRY:
                            if executor:
                                executor.submit(self._process_message, name, data)
                            else:
                                self._process_message(name, data)
                        else:
                            if self.debug:
                                print(f"Unregistered Pub/Sub task: {name}")
                else:
                    # Continue loop if no message during timeout
                    continue
        except Exception as e:
            if self.debug:
                print(f"PubSubWorker error: {e}")
        finally:
            if executor:
                executor.shutdown(wait=False)

    def _process_message(self, name: str, data: Dict[str, Any]) -> None:
        """
        Processes a single message and executes the corresponding task.

        Parameters
        ----------
        name : str
            The name of the task to execute.
        data : dict
            The data to pass to the task.

        Example
        -------
        This method is used internally and is not typically called directly.
        """
        current_thread = threading.current_thread().name
        if self.debug:
            print(f"Current thread: {current_thread}")

        func = self.TASK_REGISTRY[name]
        if self.debug:
            print(f"Executing Pub/Sub task: {name} / data: {data}")
        func(data)

class PubSubCaller:
    """
    A caller that sends tasks to a Redis Pub/Sub channel.

    Methods
    -------
    publish(name, data)
        Publishes a task to the Pub/Sub channel.
    """

    def __init__(self, redis_url: str = "redis://localhost:6379/0", channel: str = "edalite_pubsub") -> None:
        """
        Initializes the PubSubCaller with Redis connection and channel name.

        Parameters
        ----------
        redis_url : str, optional
            The URL for the Redis server (default is "redis://localhost:6379/0").
        channel : str, optional
            The name of the Redis Pub/Sub channel (default is "edalite_pubsub").

        Example
        -------
        ```python
        caller = PubSubCaller(redis_url="redis://localhost:6379/0", channel="my_channel")
        ```
        """
        self.redis = redis.Redis.from_url(redis_url)
        self.channel = channel

    def publish(self, name: str, data: Dict[str, Any]) -> None:
        """
        Publishes a task to the Pub/Sub channel.

        Parameters
        ----------
        name : str
            The name of the task to publish.
        data : dict
            The data to pass to the task.

        Example
        -------
        ```python
        caller.publish("example_task", {"key": "value"})
        ```
        """
        task_data = json.dumps({"name": name, "data": data})
        self.redis.publish(self.channel, task_data)