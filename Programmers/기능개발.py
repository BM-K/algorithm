import math

def solution(progresses, speeds):
    NoW = 0
    answer = []

    cal_time = [math.ceil((100-value)/day_work) for value, day_work in zip(progresses, speeds)]
    for idx in range(len(cal_time)):
        cur_value = cal_time[idx]

        if idx == 0:
            inner_idx = cur_value
            NoW += 1
        else:
            previous_sota = inner_idx
            if previous_sota >= cur_value:
                NoW += 1
            else:
                answer.append(NoW)
                inner_idx = cur_value
                NoW = 1
    answer.append(NoW)

    return answer


p = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(p, speeds))