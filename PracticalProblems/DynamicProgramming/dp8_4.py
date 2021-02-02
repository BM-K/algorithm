n, m = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

d = [99999] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 99999:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] != 99999:
    print(d[m])
else : print(-1)