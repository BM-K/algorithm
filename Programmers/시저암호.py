def solution(s, n):
    s = list(s)

    for idx in range(len(s)):
        if s[idx].isupper():
            s[idx] = chr((ord(s[idx]) - ord('A') + n) % 26 + ord('A'))
        elif s[idx].islower():
            s[idx] = chr((ord(s[idx]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)

s = 'a B z'
#print(ord('A'))
n = 4
print(solution(s, n))