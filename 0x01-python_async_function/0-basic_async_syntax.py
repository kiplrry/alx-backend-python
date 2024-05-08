#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    rand = random.uniform(0, max_delay)
    ans = await asyncio.sleep(rand, result=rand)
    return ans
