n = int(input())
student_list = []

for i in range(n):
    data = input().split()
    student_list.append((data[0], int(data[1])))

student_list.sort(key=lambda x:x[1])

for name in student_list:
    print(name[0], end=' ')