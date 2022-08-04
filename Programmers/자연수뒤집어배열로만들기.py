def solution(n):
    answer = [int(str(n)[n_]) for n_ in range(len(str(n))-1, -1, -1)]

    return answer

n = 83496
print(solution(n))