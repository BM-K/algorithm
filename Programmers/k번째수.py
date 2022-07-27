def solution(array, commands):
    answer = []

    for command in commands:
        start, end, position = command
        sliced_list = array[start-1:end]
        sliced_list.sort()
        answer.append(sliced_list[position-1])

    return answer