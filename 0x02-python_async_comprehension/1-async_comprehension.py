#!/usr/bin/env python3
"""
Module to use the async gen
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async func looping through an async gen
    """
    i = [i async for i in async_generator()]
    return i
