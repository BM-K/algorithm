from collections import deque


def solution(n, words):
    answer = deque([])

    for step, word in enumerate(words):
        if step != 0:
            if answer[step-1][-1] != word[0]:
                return [step % n + 1, step // n + 1]

        if word in answer:
            return [step % n + 1, step // n + 1]

        answer.append(word)

    return [0, 0]

n = 2
words = ["aba", "aba"] # [2, 1]
print(solution(n, words))
#2, ['qwe', 'eqwe', 'eqwe'] ret = [1, 2]
