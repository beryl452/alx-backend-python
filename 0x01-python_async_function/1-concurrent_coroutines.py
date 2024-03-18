#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """
    Waits for `n` random delays and returns a sorted list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value.

    Returns:
        List[int]: A sorted list of the delays.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)
    return delays    
