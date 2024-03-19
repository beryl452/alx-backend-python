#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension
    function by calculating the time taken to execute it.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    return time.time() - start_time
