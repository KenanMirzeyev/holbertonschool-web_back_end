#!/usr/bin/env python3
"""Async task runner using task_wait_random."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return completed results."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    finished = [await task for task in asyncio.as_completed(tasks)]
    return finished
