from collections import deque

def solution(arr):
    answer = []
    prev_num = -1
    queue = deque(arr)

    for i in range(len(arr)):
        cur_num = queue.popleft()

        if cur_num == prev_num:
            check = True
        else:
            check = False

        if not check:
            answer.append(cur_num)

        prev_num = cur_num

    return answer