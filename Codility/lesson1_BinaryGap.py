"""
    N = 6651
    Binary N = 1101000000101
    result: 6
"""


def solution(N):

    binary_val = str(bin(N)[2:])
    gap = [idx for idx, value in enumerate(binary_val) if value == '1']

    max_gap = -1
    for idx in range(len(gap)-1):
        cur_gap = gap[idx+1] - gap[idx] - 1
        if max_gap < cur_gap:
            max_gap = cur_gap

    if max_gap == -1:
        return 0
    else:
        return max_gap