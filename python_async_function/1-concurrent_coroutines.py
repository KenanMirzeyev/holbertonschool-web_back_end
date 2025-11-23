#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''

import asyncio
from 0-basic_async_syntax.py import wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Test file for printing the correct output of the wait_n coroutine
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    results: List[float] = []

    for coro in asyncio.as_completed(tasks):
        delay = await coro
        results.append(delay)

    return results
