#!/usr/bin/env python3
"""
module for the asyc generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async generator
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
