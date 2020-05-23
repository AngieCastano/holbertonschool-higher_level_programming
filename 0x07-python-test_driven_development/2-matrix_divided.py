#!/usr/bin/python3
"""
module to divide a matrix



"""


def matrix_divided(matrix, div):

    """ function to divide every element of a matrix into de arg div
    args: matrix: matrix to divide. div: number to divide in
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    types = [int, float]
    result = []
    pre = []
    length_back = len(matrix[0])

    if type(div) not in types:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for listt in matrix:
        pre = []
        if len(listt) != length_back:
            raise TypeError("Each row of the matrix must have the same size")
        for element in listt:
            if type(element) not in types:
                raise TypeError(message)
            else:
                pre.append(round(float(element / div), 2))
        result.append(pre)
        length_back = len(listt)
    return result
