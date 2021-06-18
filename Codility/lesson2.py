"""
    A = [1, 2, 3, 4, 5]
    K = 3
    result: [3, 4, 5, 1, 2]
"""


def solution(A, K):

    new_index = [(idx+K) % len(A) for idx in range(len(A))]
    new_arr = [float('inf')] * len(A)

    for idx in range(len(A)):
        new_arr[new_index[idx]] = A[idx]

    return new_arr