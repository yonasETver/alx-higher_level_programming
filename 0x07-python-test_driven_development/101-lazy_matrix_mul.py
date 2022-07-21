#!/usr/bin/python3
"""
  A function that multiplies 2 matrices 
  by using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplication of two matrix

    Args:
        m_a - The first list.
        m_b - The second list.
    """

    return (np.matmul(m_a, m_b))
