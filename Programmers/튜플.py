"""
def solution(s):

    split = s[1:-1]+','
    split = split.split('},')[:-1]
    for i in range(len(split)):
        split[i] += '}'

    length = []
    length_index = []
    for i in range(len(split)):
        curs = split[i].split(',')
        length.append(len(curs))
        length_index.append(i+1)

    ll = []
    for i in range(len(length_index)):
        idx = length.index(length_index[i])
        ll.append(idx)

    prev = -1
    for idx in ll:
        cur = split[idx][1:-1].split(',')

        if prev == -1:
            prev = cur
            continue
        else:
            char = set(cur) - set(prev)
            prev += list(char)

    return [int(val) for val in prev]
"""

def solution(s):
    print(s)
    s = Counter(re.findall('\d+', s))
    print(s)
    exit()
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))