

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):

        if p2.startswith(p1):
            return False
    return True

pb = ["119", "21997674223", "119295524421", "11935"]
print(solution(pb))