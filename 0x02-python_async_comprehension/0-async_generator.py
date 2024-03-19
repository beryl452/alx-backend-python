#!/usr/bin/env python3
"""3. Tasks"""
import asyncio
import random


async def async_generator() -> float:
    """
    Asynchronous generator that yields random floating-point
    numbers between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
