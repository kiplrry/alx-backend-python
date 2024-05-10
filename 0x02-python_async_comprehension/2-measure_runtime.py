#!/usr/bin/env python3
"""
Module using the comprehension function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the time taken to run the comprehension function 4 times
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter() - start
    return end
