def solution(rows, columns, queries):

    answer = []
    array = []
    value = 1
    for i in range(rows):
        cur_rows = []
        for j in range(columns):
            cur_rows.append(value)
            value += 1
        array.append(cur_rows)

    for x1, y1, x2, y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1, x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1, y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1, x1-1, -1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1, y1-1, -1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer

r = 6
c = 6
q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(r, c, q))