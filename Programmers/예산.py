
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))
