#!/usr/bin/env python3
"""
module for the asyc generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
