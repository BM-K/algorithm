def solution(n):
    source_one_count = format(n, 'b').count('1')

    cur_number = n
    while True:
        cur_number += 1
        cur_one_count = format(cur_number, 'b').count('1')

        if cur_one_count == source_one_count:
            return cur_number

n = 78
print(solution(n))