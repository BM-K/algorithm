"""
    A = [9, 3, 9, 3, 9, 7, 9]
    result: 7
"""


def solution(A):

    count = {}
    for idx, key in enumerate(A):
        try:
            count[key] += 1
        except:
            count[key] = 1

    for key, val in count.items():
        if val % 2 == 0:
            continue
        else:
            return key