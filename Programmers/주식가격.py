from collections import deque

def solution(prices):
    result = deque([])
    answer = deque(prices)
    for i in range(len(answer)):
        pop_num = answer.popleft()
        count = 0
        for j in answer:
            if j < pop_num:
                result.append(count+1)
                break
            if count + 1 == len(answer):
                result.append(count+1)
            count+=1

    result.append(0)
    return list(result)

prices = [2, 3, 1, 4, 2]
print(solution(prices))