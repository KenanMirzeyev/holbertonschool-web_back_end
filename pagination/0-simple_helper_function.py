#!/usr/bin/env python3
"""
Module
"""
def index_range(page: int, page_size: int) -> tuple:
    """
    tuple
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
