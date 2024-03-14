#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a key `k` of type str and a value `v` of type Union[int, float]
    and returns a tuple with the key and the square of the value.

    Args:
        k (str): The key.
        v (Union[int, float]): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key and the square
        of the value.
    """
    return k, v**2
