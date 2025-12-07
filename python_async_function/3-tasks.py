#!/usr/bin/env python3
"""
async
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A
    """
    return asyncio.create_task(wait_random(max_delay))
