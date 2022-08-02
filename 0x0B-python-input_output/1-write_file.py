#!/usr/bin/python3
"""
Module for write_file method.
"""

def write_file(filename="", text=""):
    """write_file writes a string to a text file.
    Args:
        filename: name of file.
        text: text to be written.
    Return: the text.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
