def solution(s):
    s_list = s.split(' ')
    s_list = sorted([int(ss) for ss in s_list])
    string = f'{s_list[0]} {s_list[-1]}'
    return string

s = "-1 -2 -3 -4"
print(solution(s))