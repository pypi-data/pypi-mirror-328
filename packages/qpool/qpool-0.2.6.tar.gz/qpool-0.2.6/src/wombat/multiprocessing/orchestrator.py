from __future__ import annotations
import asyncio
from uuid import uuid4
from annotated_types import Ge
from collections import deque
from typing import (
    List,
    Any,
    Union,
    Optional,
    Dict,
    Type,
    Callable,
    Annotated,
)
import heapq
from pydantic import BaseModel, UUID4, Field
from multiprocessing import Value, get_context

from contextlib import AsyncExitStack
from queue import Empty
from enum import Enum
from threading import Thread
import inspect
from wombat.multiprocessing.logging import setup_logging, log
from wombat.utils.errors.decorators import enforce_type_hints_contracts
from wombat.utils.dictionary import deep_merge
import logging
import time
from traceback import format_exc

from wombat.multiprocessing.models import (
    Identifiable,
    KeywordActionable,
    PositionalActionable,
    MixedActionable,
    RequiresProps,
    ProgressUpdate,
    Progresses,
    Retryable,
    Lifecycle,
    Actionable,
    TaskState,
    Evaluatable,
    ResultTaskPair,
    Prop,
    UninitializedProp,
)
from wombat.multiprocessing.tasks import (
    LogTask,
    ProgressTask,
    Task,
    ControlTask,
    ExitTask,
    EOQ,
    set_task_status,
)
from wombat.multiprocessing.queues import (
    ModelQueue,
    drain_queue,
    TaskQueue,
    LogQueue,
    ResultQueue,
    ControlQueue,
    ProgressQueue,
    explicitly_is,
    implicitly_is,
    log_task,
)
from wombat.multiprocessing.progress import run_progress, add
from wombat.multiprocessing.worker import Worker

class Orchestrator:
    @enforce_type_hints_contracts
    def __init__(
        self,
        num_workers: Annotated[int, Ge(0)],
        actions: Dict[str, Callable],
        props: Optional[Dict[str, Any]] = None,
        show_progress: bool = False,
        task_models: List[Type[Task]] | None = None,
        tasks_per_minute_limit: Optional[int] = None,
    ):
        task_models = (
            task_models if task_models is not None and len(task_models) > 0 else [Task]
        )
        self.context = get_context("spawn")
        self.tasks_per_minute_limit = self.context.Value("i", tasks_per_minute_limit // num_workers) if tasks_per_minute_limit else None

        self.total_progress_tasks = self.context.Value("i", 0)
        self.total_tasks = 0
        self.props = props if props is not None else {}
        self.started = False
        self.task_queue = TaskQueue(
            context=self.context, name="tasks", models=task_models, joinable=True
        )
        self.log_queue = LogQueue(context=self.context, name="log", joinable=True)
        self.result_queues = {}
        logger_id = uuid4()
        control_queue_name = f"control-{logger_id}"
        self.logger_control_queues = {
            f"{control_queue_name}": ControlQueue(
                context=self.context,
                name=f"{control_queue_name}",
                joinable=True,
            )
        }
        self.worker_control_queues = {}
        self.workers = []
        self.show_progress = show_progress
        self.progress_thread = None
        self.progress_queue = None
        if show_progress:
            self.progress_queue = ProgressQueue(
                context=self.context, name="progress", joinable=True
            )
            self.total_progress_tasks = self.context.Value("i", 0)
            self.remaining_progress_tasks = self.context.Value("i", 0)

        self.logger = Worker(
            context=self.context,
            name=f"logger-{logger_id}",
            id=uuid4(),
            total_progress_tasks=None,
            control_queues={"primary": self.logger_control_queues[control_queue_name]},
            task_queue=self.log_queue,
            actions={"log": log},
            props={"logger": UninitializedProp(initializer=setup_logging, use_context_manager=False)},
        )
        for i in range(num_workers):
            worker_id = uuid4()
            worker_name = f"worker-{i}"
            control_queue_name = f"control-{worker_id}"
            self.worker_control_queues[control_queue_name] = ControlQueue(
                context=self.context, name=control_queue_name, joinable=True
            )
            self.result_queues["worker-{i}"] = ResultQueue(
                context=self.context, name=f"worker-{i}-results", joinable=False
            )
            self.workers.append(
                Worker(
                    context=self.context,
                    name=worker_name,
                    id=worker_id,
                    task_id=i,
                    control_queues={
                        "primary": self.worker_control_queues[control_queue_name]
                    },
                    log_queue=self.log_queue,
                    task_queue=self.task_queue,
                    result_queue=self.result_queues["worker-{i}"],
                    progress_queue=self.progress_queue,
                    total_progress_tasks=self.total_progress_tasks,
                    actions=actions,
                    props=self.props,
                    tasks_per_minute_limit=self.tasks_per_minute_limit
                )
            )

    @enforce_type_hints_contracts
    def update_progress(self, update: ProgressUpdate):
        with self.total_progress_tasks.get_lock():
            self.total_progress_tasks.value += 1
        if self.show_progress and self.progress_queue:
            self.progress_queue.put(
                ProgressTask(
                    kwargs={
                        "update": update,
                    }
                )
            )

    @enforce_type_hints_contracts
    def log(self, message: str, level: int):
        self.log_queue.put(
            LogTask(
                kwargs={
                    "message": message,
                    "level": level,
                }
            )
        )

    async def start_workers(self):
        """Starts workers and optionally monitors progress."""
        self.started = True
        self.logger.start()
        # Start workers
        self.log(
            message=f"Started logger with id {self.logger.id} and name {self.logger.name}",
            level=logging.DEBUG,
        )

        for worker in self.workers:
            worker.start()

        if self.show_progress:
            self.progress_thread = Thread(
                target=run_progress,
                args=(
                    self.progress_queue,
                    len(self.workers),
                    self.total_progress_tasks,
                    self.remaining_progress_tasks,
                ),
                daemon=True,
            )
            self.progress_thread.start()

    def _sum_worker_finished_tasks(self, workers: List[Worker]) -> int:
        total = 0
        for worker in workers:
            with worker.finished_tasks.get_lock():
                total += worker.finished_tasks.value
        return total

    async def stop_workers(self) -> List[ResultTaskPair]:
        """Stop workers and ensure progress monitoring is stopped properly."""
        self.log(message="Waiting for workers to finish tasks", level=logging.INFO)

        self.update_progress(
            ProgressUpdate(
                task_id=-1,
                status="Waiting for workers to finish tasks",
            )
        )
        for worker in self.workers:
            total_finished_tasks = self._sum_worker_finished_tasks(self.workers)
            while self.total_tasks != total_finished_tasks:
                self.log(
                    message=f"Waiting for results to be processed {self.total_tasks} != {total_finished_tasks}",
                    level=logging.DEBUG,
                )
                await asyncio.sleep(0.1)
                total_finished_tasks = self._sum_worker_finished_tasks(self.workers)
        self.task_queue.close()
        self.task_queue.join()

        self.update_progress(
            ProgressUpdate(
                task_id=-1,
                status="Closing worker control queues",
            )
        )
        self.log(message="Closing worker control queues", level=logging.DEBUG)
        for control_queue in self.worker_control_queues.values():
            control_queue.put(ExitTask())
            control_queue.close()
            control_queue.join()

        self.update_progress(
            ProgressUpdate(
                task_id=-1,
                status="Stopping worker processes",
            )
        )
        # Ensure all worker processes are properly terminated
        self.log(message="Joining worker processes", level=logging.INFO)
        results: List[ResultTaskPair] = []
        for worker in self.workers:
            self.log(
                message=f"Draining results from worker {worker.name}",
                level=logging.DEBUG,
            )
            results.extend(drain_queue(worker.result_queue))
            worker._process.join()
            self.log(message=f"Worker-{worker.id} has exited.", level=logging.DEBUG)

        self.log(message="All workers have exited", level=logging.INFO)

        self.update_progress(
            ProgressUpdate(
                task_id=-1,
                status="Closing final resources...",
            )
        )
        # Stop progress monitoring
        if self.show_progress and self.progress_queue and self.progress_thread:
            self.update_progress(ProgressUpdate(task_id=-1, total=-1))
            self.progress_queue.join()
            self.progress_thread.join()

        # Stop the logger
        self.log_queue.close()
        self.log_queue.join()
        for queue in self.logger_control_queues.values():
            queue.put(ExitTask())
            queue.close()
            queue.join()
        self.logger._process.join()
        return results

    @enforce_type_hints_contracts
    async def add_task(self, task: Task):
        """Add task to the task queue and start workers if not started."""
        self.total_tasks += 1
        await self.add_tasks([task])

    @enforce_type_hints_contracts
    async def add_tasks(self, tasks: List[Actionable]) -> List[Task]:
        """Add task to the task queue and start workers if not started."""
        if not self.started:
            await self.start_workers()

        self.total_tasks += len(tasks)
        enqueue_failures = []
        for task in tasks:
            set_task_status(task, TaskState.queue)
            if not self.task_queue.put(task):
                enqueue_failures.append(task)
        self.total_tasks -= len(enqueue_failures)
        added = len(tasks) - len(enqueue_failures)

        # Update progress if progress monitoring is enabled
        if self.show_progress and self.progress_queue and added:
            self.update_progress(
                ProgressUpdate(
                    task_id=-1,
                    total=len(tasks),
                )
            )
        self.log(
            message=f"Added {added} tasks to the task queue. Remaining: {len(enqueue_failures)}",
            level=logging.DEBUG,
        )
        return enqueue_failures
