def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

arr = [2, 36, 1, 3]
divisor = 1
print(solution(arr, divisor))