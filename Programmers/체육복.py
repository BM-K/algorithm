def solution(n, lost, reserve):
    n_list = [0] * n

    for i in reserve:
        n_list[i-1] += 1

    for i in lost:
        n_list[i-1] -= 1

    no_answer = [x for x, y in enumerate(n_list) if y == -1]

    for i in no_answer:
        if i != 0 and i != len(n_list)-1:
            if n_list[i-1] == 1:
                n_list[i-1] -= 1
                n_list[i] += 1
            elif n_list[i+1] == 1:
                n_list[i+1] -= 1
                n_list[i] += 1
        elif i == 0:
            if n_list[i+1] == 1:
                n_list[i+1] -=1
                n_list[i] += 1
        elif i == len(n_list)-1:
            if n_list[i-1] == 1:
                n_list[i-1] -= 1
                n_list[i] += 1

    count = 0
    for i in n_list:
        if i >= 0:
            count += 1

    return count

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))