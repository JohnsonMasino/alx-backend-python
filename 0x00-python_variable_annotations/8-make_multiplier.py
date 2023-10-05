#!/usr/bin/env python3
"""
Module de task 8
"""
from typing import callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """
    creates a multiplier function
    """
    return lambda x: x * multiplier
