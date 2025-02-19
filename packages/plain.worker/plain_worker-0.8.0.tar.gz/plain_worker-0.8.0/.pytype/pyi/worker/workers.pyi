# (generated with --quick)

import concurrent.futures
import functools
import gc
import logging
import multiprocessing
import os
import time
import worker.models
from plain import models
from plain.models import transaction
from plain.utils import timezone
from typing import Any, Never

Future: type[concurrent.futures._base.Future]
Job: type[worker.models.Job]
JobRequest: type[worker.models.JobRequest]
JobResult: type[worker.models.JobResult]
JobResultStatuses: type[worker.models.JobResultStatuses]
ProcessPoolExecutor: type[concurrent.futures.process.ProcessPoolExecutor]
import_string: Any
logger: logging.Logger
partial: type[functools.partial]
request_finished: Any
request_started: Any
settings: Any

class Worker:
    _is_shutting_down: bool
    _job_results_checked_at: float
    _jobs_schedule_checked_at: float
    _stats_logged_at: float
    executor: concurrent.futures.process.ProcessPoolExecutor
    jobs_schedule: list
    max_jobs_per_process: Any
    max_pending_per_process: Any
    max_processes: Any
    queues: Any
    stats_every: Any
    def __init__(self, queues, jobs_schedule = ..., max_processes = ..., max_jobs_per_process = ..., max_pending_per_process = ..., stats_every = ...) -> None: ...
    def log_stats(self) -> None: ...
    def maybe_check_job_results(self) -> None: ...
    def maybe_log_stats(self) -> None: ...
    def maybe_schedule_jobs(self) -> None: ...
    def rescue_job_results(self) -> None: ...
    def run(self) -> Never: ...
    def shutdown(self) -> None: ...

def future_finished_callback(job_uuid: str, future: concurrent.futures._base.Future) -> None: ...
def process_job(job_uuid) -> None: ...
