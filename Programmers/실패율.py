from collections import Counter

def solution(N, stages):
    result = {}
    d = len(stages)
    for stage in range(1, N+1):
        if d != 0:
            count = stages.count(stage)
            result[stage] = count / d
            d -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda  x:result[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))