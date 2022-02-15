def solution(bridge_length, weight, truck_weights):
    answer = 0
    tob = [0] * bridge_length

    while len(tob):
        answer += 1
        tob.pop(0)

        if truck_weights:
            if sum(tob) + truck_weights[0] <= weight:
                tob.append(truck_weights.pop(0))
            else:
                tob.append(0)
    return answer


bl = 2
we = 10
tw = [7, 4, 5, 6]
print(solution(bl, we, tw))