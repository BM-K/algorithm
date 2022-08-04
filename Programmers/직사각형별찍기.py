a, b = map(int, input().strip().split(' '))

for y in range(b):
    for x in range(a):
        print("*", end='')
    print()