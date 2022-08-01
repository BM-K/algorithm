def solution(s):
    if s[0] == '-':
        #print(int(s[1:]))
        return -int(s[1:])
    else:
        return int(s)


s = '-1234'
print(solution(s))