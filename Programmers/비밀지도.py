
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j)[2:])
        print(a12)
        exit()
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))