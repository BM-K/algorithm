def bs(array, start, end, target):
    mid = (start + end) // 2

    if start > end:
        return None

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bs(array, start, end, target)

n = int(input())
total_list = list(map(int, input().split()))
total_list.sort()

m = int(input())
required_list = list(map(int, input().split()))

for val in required_list:
    result = bs(total_list, 0, len(total_list)-1, val)

    if result is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')