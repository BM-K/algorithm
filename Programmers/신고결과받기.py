def solution(id_list, report, k):
    no_dup = {}
    reported_person = []
    reported_list = {id_: 0 for id_ in id_list}
    report_list = {id_: 0 for id_ in id_list}

    for rp in report:
        person1, person2 = rp.split(' ')

        try:
            keyerror = no_dup[rp]
        except KeyError:
            reported_list[person2] += 1
            no_dup[rp] = 1

    for key, value in reported_list.items():
        if value >= k:
            reported_person.append(key)

    for people in no_dup.keys():
        person1, person2 = people.split(' ')
        if person2 in reported_person:
            report_list[person1] += 1

    answer = [val for val in report_list.values()]

    return answer