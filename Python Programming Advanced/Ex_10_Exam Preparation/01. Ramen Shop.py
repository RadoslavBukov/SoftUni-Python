"""
Input	                        Output
14, 25, 37, 43, 19              Great job! You served all the customers
58, 23, 37	                    Bowls of ramen left: 14, 6

30, 13, 45                      Out of ramen! You didn't manage to serve all customers.
70, 25, 55, 15	                Customers left: 7, 55, 15

30, 25                          Great job! You served all the customers.
20, 35
"""
from collections import deque

ramens = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while ramens and customers:
    ramen = ramens.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue
    elif ramen > customer:
        ramen -= customer
        ramens.append(ramen)
    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramens)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")