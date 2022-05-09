"""
Input	        Output	                                Comment
7               Gladiator expenses: 16.00 aureus        Trashed helmet -> 3 times
2                                                       Trashed sword -> 2 times
3                                                       Trashed shield -> 1 time
4                                                       Total: 6 + 6 + 4 = 16.00 aureus;
5

23              Gladiator expenses: 608.00 aureus
12.50
21.50
40
200
"""

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_damage = 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        expenses += helmet_price
    if i % 3 == 0:
        expenses += sword_price
        if i % 2 == 0:
            expenses += shield_price
            shield_damage += 1
            if shield_damage % 2 == 0:
                expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")