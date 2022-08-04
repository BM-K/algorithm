def solution(n):

    answer = []
    for dev in range(1, n):
        if n % dev == 1:
            answer.append(dev)

    return min(answer)

n = 5
print(solution(n))