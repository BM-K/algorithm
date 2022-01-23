
def solution(s):
    stacks = []
    for i in s:
        if len(stacks) == 0:
            stacks.append(i)
        elif stacks[-1] == i:
            stacks.pop()
        else:
            stacks.append(i)

    if len(stacks) == 0:
        return 1
    else:
        return 0
s = "baabaa"
print(solution(s))