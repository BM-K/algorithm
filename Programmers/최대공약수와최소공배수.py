from math import gcd


def lcm(x, y):
   return x * y // gcd(x,y)


def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer