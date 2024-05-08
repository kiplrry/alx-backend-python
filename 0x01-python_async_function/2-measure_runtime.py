#!/usr/bin/python3
"""
measure_time module
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Your function should return a float."""
    start = time.perf_counter()
    ans = asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
