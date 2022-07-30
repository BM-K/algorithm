from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))

    answer = list(set(answer))
    answer.sort()

    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))