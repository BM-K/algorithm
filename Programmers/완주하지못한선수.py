"""
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)

    # 4. 남은 값이
    return hashDict[sumHash]
"""

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))