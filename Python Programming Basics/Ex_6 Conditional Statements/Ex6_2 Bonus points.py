"""
Input           Output
20	            6
                26
175	            37.0
                212.0
2703	        270.3
                2973.3
15875	        1589.5
                17464.5
"""
from math import pi
number = float(input())

if number <= 100:
    bonus = 5
    if number % 2 == 0:
        bonus = bonus + 1
    if number % 10 == 5:
        bonus = bonus + 2
elif number > 100 and number <= 1000:
    bonus = number * 0.2
    if number % 2 == 0:
        bonus = bonus + 1
    if number % 10 == 5:
        bonus = bonus + 2
elif number > 1000:
    bonus = number * 0.1
    if number % 2 == 0:
        bonus = bonus + 1
    if number % 10 == 5:
        bonus = bonus + 2

print(bonus)
print(bonus + number)
