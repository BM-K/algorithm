def solution(n):
    su = '수'
    bak = '박'

    answer = ''
    for i in range(n):
        if (i+1) % 2 == 1:
            answer += su
        else:
            answer += bak
    return answer
n = 5
print(solution(n))