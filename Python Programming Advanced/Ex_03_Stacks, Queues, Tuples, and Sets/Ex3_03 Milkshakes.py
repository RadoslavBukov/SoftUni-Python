"""
Input	                            Output                                                          Comment
20, 24, -5, 17, 22, 60, 26          Great! You made all the chocolate milkshakes needed!            1) 26 == 26 -> You made chocolate milkshake. Remove both ingredients.
26, 60, 22, 17, 24, 10, 55	        Chocolate: 20                                                   2) 60 == 60 -> You made chocolate milkshake. Remove both ingredients.
                                    Milk: 10, 55                                                    3) 22 == 22 -> You made chocolate milkshake. Remove both ingredients.
                                                                                                    4) 17 == 17 -> You made chocolate milkshake. Remove both ingredients.
-10, -2, -30, 10                    Not enough milkshakes.                                          5) -5 is invalid, so it is removed before mixing.
-5	                                Chocolate: -10, -2, -30, 10                                     6) 24 == 24 -> You made chocolate milkshake. Remove both ingredients. You made enough chocolate milkshakes.
                                    Milk: empty

2, 3, 3, 7, 2                       Great! You made all the chocolate milkshakes needed!
2, 7, 3, 3, 2, 14, 6	            Chocolate: empty
                                    Milk: 14, 6
"""
from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(', ')])
milk_shakes = 0

while milk_shakes < 5 and chocolates and milk_cups:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()
    if chocolate > 0 and milk > 0:
        if chocolate == milk:
            milk_shakes += 1
        else:
            chocolates.append(chocolate-5)
            milk_cups.append(milk)
    else:
        if milk <= 0 and chocolate > 0:
            chocolates.append(chocolate)
        elif chocolate <= 0 and milk > 0:
            milk_cups.appendleft(milk)

if milk_shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print('Chocolate: empty')

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print('Milk: empty')