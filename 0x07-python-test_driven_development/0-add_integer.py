#!/usr/bin/python3
"""
A function that adds 2 integers a and b .
a and b must be integers or floats
else raise type error exeption
"""

def add_integer(a, b=98):
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
