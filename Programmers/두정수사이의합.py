def solution(a, b):
    if a == b:
        return a

    sum_ = 0
    if a < b:
        for val in range(a, b+1):
            sum_ += val
    else:
        for val in range(b, a+1):
            sum_ += val
    return sum_


a = 3
b = 5
print(solution(a, b))