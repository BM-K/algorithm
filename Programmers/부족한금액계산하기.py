def solution(price, money, count):
    needed_money = 0
    for i in range(1, count + 1):
        needed_money += price * i

    if money > needed_money:
        return 0
    else:
        return abs(money-needed_money)

price = 3
money = 20
count = 4
print(solution(price, money, count))