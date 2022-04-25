"""
Input	                Output
1                       Total cost: 37
7	                    Total spirit: 58

3                       Total cost: 558
20	                    Total spirit: 156
"""

ornament_set = 2
tree_skirt = 5
tree_girlands = 3
tree_lights = 15
quantity = int(input())
days_left = int(input())
days = 0
total_spirit = 0
total_cost = 0

while days_left > 0:
        days_left -= 1
        days += 1
        if days % 11 ==0:
                quantity += 2
        if days % 2 == 0:
                total_cost += (ornament_set * quantity)
                total_spirit += 5
        if days % 3 == 0:
                total_cost += (tree_skirt * quantity) + (tree_girlands * quantity)
                total_spirit += 13
        if days % 5 == 0:
                total_cost += (tree_lights * quantity)
                total_spirit += 17
                if days % 3 == 0:
                        total_spirit += 30
        if days % 10 == 0:
                total_spirit -= 20
                total_cost += (tree_skirt + tree_girlands + tree_lights)
                if days_left == 0:
                        total_spirit -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')