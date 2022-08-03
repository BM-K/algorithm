def solution(s):
    s_ord_list = [ord(s_) for s_ in s]
    s_ord_list = sorted(s_ord_list, reverse=True)
    answer = [chr(s_) for s_ in s_ord_list]

    return ''.join(answer)

s = "Zbcdefg"

print(solution(s))