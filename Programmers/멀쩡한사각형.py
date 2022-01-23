import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))

answer = solution(8, 12)
print(answer)