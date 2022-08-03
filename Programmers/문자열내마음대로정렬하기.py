def solution(strings, n):
    strings = sorted(strings)
    inner_char = [(string[n], i) for i, string in enumerate(strings)]
    sorted_strings = sorted(inner_char, key=lambda x:x[0])

    answer = []
    for _, index in sorted_strings:
        answer.append(strings[index])

    return answer

n = 2
strings = ["abce", "abcd", "cdx"]
print(solution(strings, n))