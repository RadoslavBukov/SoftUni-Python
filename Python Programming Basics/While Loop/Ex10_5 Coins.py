"""
Input       Output
1.23        4

2           1

0.56        3

2.73        5
"""
change = float(input())
number_coins = 0

while change > 0:
    if change - 2.00 >= 0:
        change -= 2.00
        change = round(change, 2)
        number_coins += 1
    elif change - 1.00 >= 0:
        change -= 1.00
        change = round(change, 2)
        number_coins += 1
    elif change - 0.50 >= 0:
        change -= 0.50
        change = round(change, 2)
        number_coins += 1
    elif change - 0.20 >= 0:
        change -= 0.20
        change = round(change, 2)
        number_coins += 1
    elif change - 0.10 >= 0:
        change -= 0.10
        change = round(change, 2)
        number_coins += 1
    elif change - 0.05 >= 0:
        change -= 0.05
        change = round(change, 2)
        number_coins += 1
    elif change - 0.02 >= 0:
        change -= 0.02
        change = round(change, 2)
        number_coins += 1
    elif change - 0.01 >= 0:
        change -= 0.01
        change = round(change, 2)
        number_coins += 1

print(number_coins)

