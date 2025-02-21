"""
Thread pool implementation with advanced task management and prioritization.
"""

import threading
from queue import PriorityQueue
from typing import Any, Callable, Optional, Dict, List, Tuple
from concurrent.futures import Future
import logging
import time
import multiprocessing

logger = logging.getLogger(__name__)

class PrioritizedItem:
    def __init__(self, priority: int, item: Any):
        self.priority = priority
        self.item = item
        self.timestamp = time.time()

    def __lt__(self, other):
        if not isinstance(other, PrioritizedItem):
            return NotImplemented
        return (self.priority, self.timestamp) < (other.priority, other.timestamp)

class Task:
    def __init__(self, priority: int, func: Callable, args: tuple = (), kwargs: Optional[Dict] = None):
        """
        Initialize a task with priority and function.

        Args:
            priority: Task priority (lower number = higher priority)
            func: Function to execute
            args: Function arguments
            kwargs: Function keyword arguments
        """
        self.priority = priority
        self.func = func
        self.args = args
        self.kwargs = kwargs if kwargs is not None else {}
        self.future = Future()
        self.created_at = time.time()

class Worker(threading.Thread):
    def __init__(self, task_queue: PriorityQueue, pool: 'ThreadPool'):
        """Initialize worker thread."""
        super().__init__(daemon=True)
        self.task_queue = task_queue
        self.pool = pool
        self.running = True

    def run(self):
        """Process tasks from the queue."""
        while self.running:
            try:
                prioritized_item = self.task_queue.get(timeout=1)
                if prioritized_item is None or not self.running:  # Poison pill
                    break

                task = prioritized_item.item
                if task is None:
                    continue

                try:
                    result = task.func(*task.args, **task.kwargs)
                    task.future.set_result(result)
                except Exception as e:
                    logger.error(f"Task execution failed: {str(e)}")
                    task.future.set_exception(e)
                finally:
                    self.task_queue.task_done()

            except Exception:
                continue

class ThreadPool:
    def __init__(self, max_workers: Optional[int] = None):
        """
        Initialize thread pool.

        Args:
            max_workers: Maximum number of worker threads
        """
        self.max_workers = max_workers or (multiprocessing.cpu_count() * 2)
        self.task_queue = PriorityQueue()
        self.workers: List[Worker] = []
        self.lock = threading.Lock()
        self.running = True
        self._start_workers()

    def _start_workers(self):
        """Start worker threads."""
        with self.lock:
            while len(self.workers) < self.max_workers:
                worker = Worker(self.task_queue, self)
                worker.start()
                self.workers.append(worker)

    def submit(self, func: Callable, *args, priority: int = 5, **kwargs) -> Future:
        """
        Submit a task to the thread pool.

        Args:
            func: Function to execute
            *args: Function arguments
            priority: Task priority (1-10, lower = higher priority)
            **kwargs: Function keyword arguments

        Returns:
            Future: Future object for getting the result
        """
        if not self.running:
            raise RuntimeError("ThreadPool is shutting down")

        task = Task(priority, func, args, kwargs)
        self.task_queue.put(PrioritizedItem(priority, task))
        return task.future

    def map(self, func: Callable, iterable: List[Any], priority: int = 5) -> List[Future]:
        """
        Map a function over an iterable.

        Args:
            func: Function to execute
            iterable: Iterable of arguments
            priority: Task priority

        Returns:
            List[Future]: List of Future objects
        """
        return [self.submit(func, item, priority=priority) for item in iterable]

    def shutdown(self, wait: bool = True):
        """
        Shutdown the thread pool.

        Args:
            wait: Wait for all tasks to complete
        """
        self.running = False

        # Send poison pills to all workers
        for _ in self.workers:
            self.task_queue.put(PrioritizedItem(0, None))

        if wait:
            self.task_queue.join()

        for worker in self.workers:
            worker.running = False
            if worker.is_alive():
                worker.join()

        self.workers.clear()