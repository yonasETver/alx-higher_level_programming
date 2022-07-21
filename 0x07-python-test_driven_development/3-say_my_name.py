#!/usr/bin/python3
"""
 A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ 
    Print the name 
    Args:
        first_name - String  first name.
        last_name  - String  last name.
    raise:
        raise type error if parameter are not 
        string else print name 
        
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
