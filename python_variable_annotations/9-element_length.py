#!/usr/bin/env python3
"""
Module that defines element_length function with type annotations.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element from lst and its length.
    """
    return [(i, len(i)) for i in lst]
