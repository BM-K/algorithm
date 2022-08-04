from itertools import combinations
import math


def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def solution(nums):
    jo = []
    for i in combinations(nums, 3):
        j = sum(i)
        if primenumber(j):
            jo.append(j)

    return len(jo)

nums = [1, 2, 3, 4]
print(solution(nums))