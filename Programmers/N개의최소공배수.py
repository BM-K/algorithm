from math import gcd


def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))

        if len(arr) == 1:
            return arr[0]


arr = [2,6,8,14]

print(solution(arr))