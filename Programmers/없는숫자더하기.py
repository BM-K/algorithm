def solution(numbers):
    original = [0,1,2,3,4,5,6,7,8,9]
    charzip = set(original) - set(numbers)

    return sum(charzip)

numbers = [5,8,4,0,6,7,9]
print(solution(numbers))