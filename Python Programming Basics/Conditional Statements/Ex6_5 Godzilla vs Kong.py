"""
Input               Output
20000               Action!
120                 Wingard starts filming with 11340.00 leva left.
55.5

15437.62            Action!
186                 Wingard starts filming with 4186.33 leva left.	Сума за декор: 10% от 15437.62 = 1543.762 лв.
57.99

9587.88             Not enough money!
222                 Wingard needs 2495.77 leva more.
55.68
"""
budget = float(input())
number_extras = int(input())
clothes_price = float(input())

decor = budget*0.1
clothes = number_extras*clothes_price

if number_extras>= 150:
    clothes -= clothes*0.1

if decor+clothes > budget:
    print('Not enough money!')
    print(f'Wingard needs {(decor+clothes)-budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget-(decor + clothes):.2f} leva left.')