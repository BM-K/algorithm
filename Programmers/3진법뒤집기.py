def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        print(n, rest)
        answer += str(rest)
    answer = int(answer, 3)

    return answer
n = 45
print(solution(n))