"""
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    result: 6
"""


def solution(X, A):

    may_consist = [0] * (X+1)

    count = 0
    for idx, val in enumerate(A):
        if may_consist[val] == 0:
            may_consist[val] += 1
            count += 1
        if count == X:
            return idx
    return -1
