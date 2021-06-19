"""
    A = [2, 3, 1, 5]
    result: 4
"""


def solution(A):
    may_consist = [i + 1 for i in range(len(A) + 1)]

    complement = int(list(set(may_consist) - set(A))[0])
    return complement