def solution(phone_number):
    masking = phone_number[-4:]
    length = len(phone_number) - len(masking)
    str = '*' * length + masking

    return str

pn = "01033334444"
print(solution(pn))