#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for item in matrix:
        item = list(map(lambda x: x*x, item))
        res.append(item)
         return res
