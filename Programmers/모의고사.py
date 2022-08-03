def solution(answers):
    one_p = [1, 2, 3, 4, 5] * 2000
    two_p = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three_p = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    one_p = one_p[:len(answers)]
    two_p = two_p[:len(answers)]
    three_p = three_p[:len(answers)]

    p_list = {1:0, 2:0, 3:0}
    for my, tr in zip(one_p, answers):
        if my == tr:
            p_list[1] += 1
    for my, tr in zip(two_p, answers):
        if my == tr:
            p_list[2] += 1
    for my, tr in zip(three_p, answers):
        if my == tr:
            p_list[3] += 1

    sorted_dict = sorted(p_list.items(), key=lambda item: item[1])
    if sorted_dict[-1][-1] == sorted_dict[-2][-1]:
        idx=[]
        for i in range(len(sorted_dict)):
            if sorted_dict[i][-1] == sorted_dict[-1][-1]:
                idx.append(sorted_dict[i][0])
        return idx
    else:
        return [sorted_dict[-1][0]]

answers = [1,3,2,4,2]
print(solution(answers))