def solution(sizes):
    one_max = []
    two_max = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        one_max.append(sizes[i][0])
        two_max.append(sizes[i][1])

    return max(one_max) * max(two_max)

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))