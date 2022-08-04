def solution(numbers, hand):
    only_left = [1, 4, 7]
    only_right = [3, 6, 9]

    phone_dict = {1:[0, 0], 2:[0, 1], 3:[0, 2],
                  4:[1, 0], 5:[1, 1], 6:[1, 2],
                  7:[2, 0], 8:[2, 1], 9:[2, 2],
                  '*':[3, 0], 0:[3, 1], '#':[3, 2]}

    answer = ''
    where_left = phone_dict['*']
    where_right = phone_dict['#']

    for number in numbers:
        if number in only_right:
            answer += 'R'
            where_right = phone_dict[number]
            continue
        if number in only_left:
            answer += 'L'
            where_left = phone_dict[number]
            continue

        dist_left = 0
        dist_right = 0
        for i in range(2):
            dist_left += abs(phone_dict[number][i] - where_left[i])
            dist_right += abs(phone_dict[number][i] - where_right[i])

        if dist_right == dist_left:
            if hand == 'right':
                where_right = phone_dict[number]
                answer += 'R'
            else:
                where_left = phone_dict[number]
                answer += 'L'
            continue

        if dist_right < dist_left:
            where_right = phone_dict[number]
            answer += 'R'
        if dist_right > dist_left:
            where_left = phone_dict[number]
            answer += 'L'

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))