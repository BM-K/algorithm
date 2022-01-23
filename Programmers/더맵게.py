import heapq

def solution(scoville, K):

    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix_val = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, mix_val)

        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer

scovile = [1, 3, 5, 4, 8, 7]
K = 7
print(solution(scovile, K))