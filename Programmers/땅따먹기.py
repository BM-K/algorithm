def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])

land = [[1,2,3,5]
,[5,6,7,100]
,[4,3,2,1]]
print(solution(land))