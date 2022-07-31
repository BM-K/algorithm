def solution(a, b):
    answer = 0

    for n1, n2 in zip(a, b):
        answer += n1 * n2

    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a, b))