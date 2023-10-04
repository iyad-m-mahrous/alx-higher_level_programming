#!/usr/bin/python3
""" a function that multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """def lazy_matrix_mul(m_a, m_b):

    Args:
        m_a (list): 2D Matrix
        m_b (list): 2D Matrix
    """

    return (np.matmul(m_a, m_b))
