"""
Input               Output
Roses               Not enough money, you need 25.00 leva more.
55
250

Tulips              Hey, you have a great garden with 88 Tulips and 50.56 leva left.
88
260

Narcissus           Not enough money, you need 50.55 leva more.
119
360
"""

flower_type = str(input())
number = int(input())
budget = int(input())

rose = 5
dahlia = 3.8
tulip = 2.8
narcissus = 3
gladiolus = 2.5

if flower_type == "Roses":
    if number > 80:
        price = (number*rose) - (number*rose)*0.1
    else:
        price = (number*rose)
elif flower_type == "Dahlias":
    if number > 90:
        price = (number*dahlia) - (number*dahlia)*0.15
    else:
        price = (number*dahlia)
elif flower_type == "Tulips":
    if number > 80:
        price = (number*tulip) - (number*tulip)*0.15
    else:
        price = (number*tulip)
elif flower_type == "Narcissus":
    if number < 120:
        price = (number*narcissus) + (number*narcissus)*0.15
    else:
        price = (number*narcissus)
elif flower_type == "Gladiolus":
    if number < 80:
        price = (number*gladiolus) + (number*gladiolus)*0.2
    else:
        price = (number*gladiolus)

if budget >= price:
    print(f"Hey, you have a great garden with {number} {flower_type} and {budget-price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price-budget:.2f} leva more.")
