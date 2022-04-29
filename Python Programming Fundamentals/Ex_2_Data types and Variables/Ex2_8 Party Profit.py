"""
Input	        Output
3               3 companions received 90 coins each.
5

15              19 companions received 102 coins each.
30
"""

import math
group_size = int(input())
days = int(input())
coins = 0

for i in range(1, days+1):
    if i % 15 == 0:
        group_size += 5
    if i % 10 == 0:
        group_size -= 2
    coins += (50 - (group_size * 2))
    if i % 3 == 0:
        coins -= group_size*3
    if i % 5 == 0:
        coins += (group_size*20)
        if i % 3 == 0:
            coins -= group_size*2

print(f"{group_size} companions received {math.floor(coins/group_size)} coins each.")