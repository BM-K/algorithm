import operator

location = input()
row = location[1]
col = location[0]

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
location = [int(row)-1, alpha.index(col)]
rule = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
count = 0

for i in range(len(rule)):
    temp_lo = list(map(operator.add, location, rule[i]))

    if temp_lo[0] < 0 or temp_lo[1] < 0 or temp_lo[0] > 7 or temp_lo[1] > 7:
        continue
    count += 1

print(count)