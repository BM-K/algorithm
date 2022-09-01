from itertools import product


def solution(word):
    answer = []
    d = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for cwr in product(d, repeat=i):
            answer.append(''.join(cwr))

    answer = sorted(answer)

    return answer.index(word)+1

word = 'I'
print(solution(word))