
import math
from itertools import product, permutations

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 0 or x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(numbers):

    numbers = ' '.join(numbers).split(' ')
    johap = []
    for idx in range(len(numbers)):
        johap += [''.join(i) for i in list(permutations(numbers, idx+1))]

    removed_zero_duple = list(set([int(val) for val in johap]))
    answer = sum([is_prime_number(val) for val in removed_zero_duple])

    return answer

n = "013"
print(solution(n))

# a = [''.join(i) for i in list(product(['A', 'C', 'G', 'T'], repeat=4))]
# print(a)