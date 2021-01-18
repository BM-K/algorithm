
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

"""
n = int(input())
rule = list(map(str, input().split()))
map_ = []
x = 0
y = 0

for row in range(n):
    temp = []
    for col in range(n):
        coordinate = (row+1, col+1)
        temp.append(coordinate)
    map_.append(temp)

for token in rule:
    if token == 'R':
        yy = 1
        xx = 0
    elif token == 'L':
        yy = -1
        xx = 0
    elif token == 'U':
        xx = -1
        yy = 0
    else:
        xx = +1
        yy = 0
    x += xx
    y += yy

    if x < 0 or x>=n:
        x -= xx
    elif y < 0 or y>=n:
        y -= yy

print(map_[x][y])
"""
