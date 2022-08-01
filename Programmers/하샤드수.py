def solution(x):
    sum = 0
    for n in str(x):
        sum += int(n)

    if x % sum == 0:
        return True
    else:
        return False

x = 11
print(solution(x))