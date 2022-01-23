
def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
        print(q)
    return q.count(target)

n = [1,1,1,1,1]
t = 3
print(solution(n, t))