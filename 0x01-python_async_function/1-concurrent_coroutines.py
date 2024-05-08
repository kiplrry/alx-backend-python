#!/usr/bin/env python3
"""
this module implements write an async routine
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    akes in 2 int arguments (in this order): n and max_delay.
    it will spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be
    in ascending order without using sort() because of concurrency.
    """
    i = 0
    arr = []
    while i < n:
        arr.append(await wait_random(max_delay))
        i += 1
    lst = asyncio.gather(*arr)

    return lst
