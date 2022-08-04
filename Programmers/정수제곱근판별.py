import math

def solution(n):
    val = math.sqrt(n)
    left, right = str(val).split('.')

    if right == '0':
        return (int(left)+1) ** 2
    else:
        return -1

n = 121
print(solution(n))