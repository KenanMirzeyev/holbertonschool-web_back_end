#!/usr/bin/env python3
"""
Run multiple task_wait_random tasks.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    Run task_wait_random n times and return sorted delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
