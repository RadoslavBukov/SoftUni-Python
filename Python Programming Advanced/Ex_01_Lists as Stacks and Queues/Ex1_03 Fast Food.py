"""
Input                                   Output
348                                     54
20 54 30 16 7 9                         Orders complete

499                                     100
57 45 62 70 33 90 88 76 100 50          Orders left: 76 100 50
"""
from collections import deque

quantity_food = int(input())
food_each_order = list(map(int, input().split()))

q_food_each_order = deque()
for _ in food_each_order:
    q_food_each_order.append(_)

print(max(food_each_order))

while q_food_each_order:
    if q_food_each_order[0] <= quantity_food:
        quantity_food -= q_food_each_order.popleft()
    else:
        break

if q_food_each_order:
    print(f"Orders left: ",end="")
    for _ in range(len(q_food_each_order)):
        print(q_food_each_order.popleft(),end=' ')
else:
    print("Orders complete")