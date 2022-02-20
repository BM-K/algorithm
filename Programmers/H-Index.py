def solution(citations):
    h_index = 0
    citations.sort()

    for step, val in enumerate(range(max(citations)+1)):
        check_sum = sum([val<=v for v in citations])
        if val <= check_sum:
            h_index = val
        else:
            break

    return h_index

citations = [6,5,4,1,0]
print(solution(citations))
#[6,5,4,1,0]