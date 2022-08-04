def solution(s):
    s = s.lower()
    string_list = s.split(' ')
    answer = []
    for i, word in enumerate(string_list):
        if word == '':
            answer.append('')
        else:
            string = word[0].upper() + word[1:]
            answer.append(string)

    return ' '.join(answer)


s = "3people unFollowed me"
print(solution(s))