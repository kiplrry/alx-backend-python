#!/usr/bin/env python3
"""Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """func to return a func"""
    def mult(num: float) -> float:
        return num * multiplier
    return mult
