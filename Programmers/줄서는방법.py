
from math import factorial
def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    order = []
    k -= 1
    for i in range(n-1, -1, -1):
        print(i)
        temp = factorial(i)
        q, r = divmod(k, temp)
        k = r
        order.append(q)

    for idx in order:
        answer.append(nums.pop(idx))

    return answer

n = 3
k = 5
print(solution(n, k))