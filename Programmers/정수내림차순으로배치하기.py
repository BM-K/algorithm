def solution(n):

    n_list = [(n_) for n_ in str(n)]
    n_list = sorted(n_list, reverse=True)

    return int(''.join(n_list))

n = 118372
print(solution(n))