

def solution(s):
    mapping = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = s
    for key, value in mapping.items():
        answer = answer.replace(key, value)
    return int(answer)

s = "one4seveneight"
print(solution(s))