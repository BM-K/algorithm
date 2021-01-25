n = int(input())
num_list = [-1] * n

for i in range(len(num_list)):
    num_list[i] = input()
num_list.sort(reverse=True)
print(' '.join(num_list))
