def solution(s):
    answer = []
    splited_s = s.split(' ')
    for i in range(len(splited_s)):
        cur_s = ''
        for j in range(len(splited_s[i])):
            if j % 2 == 0:
                cur_s += splited_s[i][j].upper()
            else:
                cur_s += splited_s[i][j].lower()
        answer.append(cur_s)

    return ' '.join(answer)

s = "try hello world"
print(solution(s))