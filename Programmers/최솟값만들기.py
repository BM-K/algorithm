def solution(A,B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=False)

    total = 0
    for a, b in zip(A, B):
        total += a * b

    return total

A = [1, 2]
B = [3, 4]
print(solution(A, B))