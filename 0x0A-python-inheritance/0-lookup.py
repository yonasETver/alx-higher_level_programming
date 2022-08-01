#!/usr/bin/python3
"""
A function that returns the list of available
"""

def lookup(obj):
    """retrun list of attributes and methods of `obj`
    Args:
        obj (Any): object
    Returns:
        list: list of attributes and members
    """
    return dir(obj)
