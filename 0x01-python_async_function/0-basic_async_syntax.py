#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random
delay and returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (inclusive)
    seconds and return it.

    Args:
        max_delay: The maximum delay in seconds (default: 10).

    Returns:
        The random delay in seconds (float value).
    """
    rand = random.uniform(0, max_delay)
    ans = await asyncio.sleep(rand, result=rand)
    return ans
