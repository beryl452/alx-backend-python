#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Calculate the sum of a mixed list of floats and integers.

    Args:
        mxd_lst (List[float | int]): The mixed list of floats and integers.

    Returns:
        float: The sum of the mixed list.

    """
    return float(sum(mxd_lst))
