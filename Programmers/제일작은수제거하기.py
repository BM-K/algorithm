def solution(arr):

    mini = min(arr)
    del arr[arr.index(mini)]

    if len(arr) == 0:
        return [-1]
    else:
        return arr


arr = [10]
print(solution(arr))