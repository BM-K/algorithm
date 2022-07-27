def solution(lottos, win_nums):
    score = [6, 5, 4, 3, 2, 1]

    intersection = len(set(lottos) & set(win_nums))
    num_of_zero = lottos.count(0)

    best = intersection + num_of_zero
    worst = intersection

    if best in [0, 1]:
        return [6, 6]

    best = score[best-1]

    if worst in [0, 1]:
        worst = 6
    else:
        worst = score[worst-1]

    return [best, worst]