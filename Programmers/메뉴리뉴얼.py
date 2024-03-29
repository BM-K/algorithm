from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi

        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2, 3, 4]
print(solution(orders, course))