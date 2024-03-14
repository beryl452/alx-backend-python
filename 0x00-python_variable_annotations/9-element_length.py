#!/usr/bin/env python3
""" Let's duck type an iterable object mandatory"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a given list.

    Args:
        lst: A list of elements.

    Returns:
        A list of tuples, where each tuple contains an element
        from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
