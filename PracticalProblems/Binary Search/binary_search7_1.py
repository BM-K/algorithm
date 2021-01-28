def bs(array, start, end, target):
    mid = (start + end) // 2

    if start > end:
        return 999

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bs(array, start, end, target)

li = [0, 2, 4, 6, 8, 10, 12, 14]
result = bs(li, 0, len(li)-1, 11)

if result == 999:
    print("못찾음")
else:
    print(li[result])