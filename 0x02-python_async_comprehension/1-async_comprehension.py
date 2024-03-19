#!/usr/bin/env python3
"""1. Async Comprehensions"""
import random
from typing import List


async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """
    This function performs an asynchronous comprehension
    on the result of an async generator.

    Returns:
        A list of floats generated from the async generator.
    """
    return [i async for i in async_generator()]
