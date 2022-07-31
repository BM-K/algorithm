def solution(a, b):
    answer = 0
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(a - 1):
        answer += months[i]

    answer += b - 1
    answer = answer % 7

    return days[answer]