def solution(s):
    count_bin_change, count_del_zero = 0, 0
    while s != '1':
        count_del_zero += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        count_bin_change += 1

    return [count_bin_change, count_del_zero]
