import math


def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(n):
    answer = []
    for i in range(2, n+1):
        check = primenumber(i)
        if check:
            answer.append(i)
    return len(answer)

n = 10
print(solution(n))