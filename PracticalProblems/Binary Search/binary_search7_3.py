def bs(array, start, end, target, result):
    mid = (start + end) // 2
    total = 0

    if start > end:
        return None

    for x in array:
        if x > mid:
            total += x - mid

    if total == m:
        return mid
    elif total > m:
        start = mid + 1
    else:
        end = mid - 1

    result[0] = mid
    return bs(array, start, end, target, result)


n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = [-1]
val = bs(array, 0, max(array), m, result)

if val == None:
    print(result[0])
else:
    print(val)
