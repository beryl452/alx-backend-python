#!/usr/bin/env python3
"""2. Measure the runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken to execute the wait_n function n times.

    Args:
        n (int): The number of times to execute the wait_n function.
        max_delay (int): The maximum delay for each execution of the wait_n function.

    Returns:
        float: The average time taken to execute the wait_n function.

    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
