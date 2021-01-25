n, k = map(int, input().split())
A = []
B = []
for i in range(2):
    if i == 0:
        A = list(map(int, input().split()))
    else:
        B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:break
print(sum(A))