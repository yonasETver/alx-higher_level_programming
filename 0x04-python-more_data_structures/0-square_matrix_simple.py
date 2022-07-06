#!/usr/bin/python3

"""function that computes the square value 
of all integers of a matrix."""

def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
    return squared
