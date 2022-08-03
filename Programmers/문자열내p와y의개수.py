from collections import Counter

def solution(s):
    s = s.lower()
    s_list = [s_ for s_ in s]
    s_dict = dict(Counter(s_list))

    if 'p' not in s_list and 'y' not in s_list:
        return True

    try:
        num_of_p = s_dict['p']
        num_of_y = s_dict['y']
    except KeyError:
        return False

    if num_of_p == num_of_y:
        return True
    else:
        return False

s = "pPoooyY"
print(solution(s))