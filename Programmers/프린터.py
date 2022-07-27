from collections import deque

def solution(priorities, location):

    queue = deque(priorities)
    mapping_list = deque(['a'*(i+1) for i in range(len(queue))])
    priority_docs = mapping_list[location]

    iter_ = 0
    while (1):
        first_val = queue.popleft()
        first_map = mapping_list.popleft()
        checking = [first_val < val for val in queue]

        if sum(checking) >= 1:
            queue.append(first_val)
            mapping_list.append(first_map)
        else:
            iter_ += 1
            if first_map == priority_docs:
                return iter_

p = [9, 4, 7, 3]
l = 1
print(solution(p, l))