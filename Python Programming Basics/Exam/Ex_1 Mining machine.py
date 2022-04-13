"""
Input       Output
700         10295
15          440
0.20
2

800         11530
10          146
0.32
6.4
"""
import math
videocard_price = int(input())
adapter_price = int(input())
videocard_current_price = float(input())
profit_per_day = float(input())

sum_cost = (13 * videocard_price) + (13 * adapter_price) + 1000
day_profit = 13 * (profit_per_day-videocard_current_price)

print(sum_cost)
print(math.ceil(sum_cost/day_profit))
