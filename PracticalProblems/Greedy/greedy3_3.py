
row, col = map(int, input().split())
min_list = []

for i in range(row):
    card_map = list(map(int, input().split()))
    min_list.append([i, min(card_map)])

min_list.sort(key=lambda x:x[1], reverse=True)
print(min_list[0][1])