def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)

    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str(''.join(numbers))

numbers = [0]
print(solution(numbers))
