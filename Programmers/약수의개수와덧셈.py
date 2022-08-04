def yak(num):
    y = []
    for i in range(1, num + 1):
        if num % i == 0:
            y.append(i)
    return y

def solution(left, right):
    answer = 0

    for value in range(left, right+1):
        num = len(yak(value))

        if num % 2 == 0:
            answer += value
        else:
            answer -= value

    return answer

left = 13
right = 17
print(solution(left, right))