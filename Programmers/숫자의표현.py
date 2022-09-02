from collections import deque


def solution(n):

    numbers = deque([v for v in range(1, n+1)])
    answer = []
    count = 0

    while True:
        if len(numbers) == 1:break

        for num in numbers:
            if sum(answer) >= n:
                numbers.popleft()
                answer = []
                break
            if num + sum(answer) == n:
                count += 1
                numbers.popleft()
                answer.append(num)
                answer = []
                break

            answer.append(num)

    return count+1

n = 15
print(solution(n))