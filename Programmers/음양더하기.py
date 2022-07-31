def solution(absolutes, signs):

    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num

    return answer

absolutes = [4,7,12]
signs = [True, False, True]
print(solution(absolutes, signs))