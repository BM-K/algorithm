def solution(x, n):
    answer = [x]
    for i in range(1, n):
        answer.append(answer[i-1] + x)
    return answer

x = -4
n = 2
print(solution(x, n))