import re

def solution(new_id):

    answer = ''

    special_tokens = ['-', '_', '.']
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for s in new_id:
        if s.isalpha() or s.isdigit() or s in special_tokens:
            answer+=s

    # 3단계 https://tmdrl5779.tistory.com/124
    # https://mizykk.tistory.com/116
    answer = re.sub('(([.])\\2{1,})', '.', answer)

    # 4단계
    answer = answer.strip('.')

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    answer = answer[:15].strip('.')

    # 7단계
    if len(answer) < 3:
        for i in range(3-len(answer)):
            answer += answer[-1]

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))
