"""
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b
"""


def fib(n):
    fibList=[1, 1]
    if n==1:
        return 1
    if n==2:
        return 2

    for i in range(2,n):
        fibList.append((fibList[i-1] + fibList[i-2])%1000000007 )
    return fibList


def solution(n):
    return fib(n+1)[-1]

n = 4
print(solution(n))