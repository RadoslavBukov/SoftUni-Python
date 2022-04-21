"""
Input               Output                                      Comments
1                   The price for the coffee is: $367.20        We are given only 1 order. Then we  use the formulas:
1.53                Total: $367.20                              order price = 30 * 8 * 1.53 = 367.20
30
8

2                   The price for the coffee is: $464.07
4.99                The price for the coffee is: $54.25
31                  Total: $518.32
3
0.35
31
5

1                   The price for the coffee is: $123800.33
9.223               Total: $123800.33
31
433
"""

number = int(input())
total_price = 0

for i in range(1, number+1):
    price_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    order_price = price_capsule*days*capsule_count
    total_price += order_price
    print(f'The price for the coffee is: ${order_price:.2f}')
print(f'Total: ${total_price:.2f}')
