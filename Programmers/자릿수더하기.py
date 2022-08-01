def solution(n):
    answer = 0
    for i in range(len(str(n))): answer+=int(str(n)[i])
    return answer

N = 123
print(solution(N))