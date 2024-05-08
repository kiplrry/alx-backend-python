#!/usr/bin/env python3
"""
module 4-tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    akes in 2 int arguments (in this order): n and max_delay.
    it will spawn wait_random n times with the specified max_delay.

    task_wait_n should return the list of all the delays (float values).
    The list of the delays should be
    in ascending order without using sort() because of concurrency.
    """

    arr = await asyncio.gather(*(task_wait_random(max_delay)
                                 for _ in range(n)))

    return sorted(arr)
