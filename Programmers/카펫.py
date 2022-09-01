def solution(brown, yellow):

    total = brown + yellow
    sol = []

    for col in range(3, total):
        row = int(total / col)

        if( ((row * col) == total) & (row >= col) & ( ((col-2) * (row-2)) == yellow)):
            sol = [row, col]
            break

    return sol

b = 10
y = 2
print(solution(b, y))