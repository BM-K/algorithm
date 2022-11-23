"""
    N = 6651
    Binary N = 1101000000101
    result: 6
"""

def solution(N):
    answer = []
    binary = str(format(N, 'b'))

    target_index = [step for step, idx in enumerate(binary) if idx == str(1)]

    if len(target_index) == 1:
        return 0
    else:
        first_value = target_index[0]
        for idx in range(1, len(target_index)):
            answer.append(abs(first_value - target_index[idx]))
            first_value = target_index[idx]
        return max(answer) - 1

n = 15
print(solution(n))
