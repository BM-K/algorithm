import operator

N, M = map(int, input().split())
row, col, look = map(int, input().split())
map_ = []

for i in range(N):
    temp = []
    temp += list(map(int, input().split()))
    map_.append(temp)

gone_location = [[row, col]]
location = [row, col]
count = 0
rule = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
    temp_lo = list(map(operator.add, location, rule[look]))

    if map_[temp_lo[0]][temp_lo[1]] == 1 or temp_lo in gone_location:
        look -= 1
        if look < 0 : look = 3
    else:
        location = temp_lo
        gone_location.append(location)
        count = 0

    count += 1

    if count == 5:
        location = list(map(operator.add, location, [-1, 0]))
        if map_[location[0]][location[1]] == 1 or location in gone_location : break
        count = 0

print(len(gone_location))