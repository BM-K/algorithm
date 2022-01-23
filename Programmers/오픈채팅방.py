record =\
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]


def solution(record):
    chat = []
    action_list = []
    user_list = {}
    for step, action in enumerate(record):

        action = action.split(' ')
        if len(action) == 3:
            act, id_, name = action

            user_list[id_] = name
            if act == "Enter":
                c = str(id_)
                chat.append(c)
                action_list.append("님이 들어왔습니다.")

        else:
            act, id_ = action
            c = str(id_)
            chat.append(c)
            action_list.append("님이 나갔습니다.")

    ll = []
    for step, id in enumerate(chat):
        chat[step] = chat[step].replace(str(id), user_list[id])
        c_c = chat[step]+action_list[step]
        ll.append(c_c)

    return ll

solution(record)



"""
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
"""