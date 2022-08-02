#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """ module write_file
    Returns the number of characters 
    """
    with open(filename, 'w') as f:
        return f.write(text)
