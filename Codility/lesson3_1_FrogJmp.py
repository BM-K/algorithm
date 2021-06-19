"""
    X = 10
    Y = 140
    D = 30
    result: 5
"""

import math


def solution(X, Y, D):
    length = Y - X
    quotient = length / D
    remainder = length % D

    if remainder == 0:
        return int(quotient)
    else:
        return math.ceil(quotient)