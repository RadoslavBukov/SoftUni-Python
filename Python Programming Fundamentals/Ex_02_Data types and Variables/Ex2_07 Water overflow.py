"""
Input	        Output                              Input           Output
5               Insufficient capacity!              4               Insufficient capacity!
20              240                                 250             Insufficient capacity!
100                                                 10              Insufficient capacity!
100                                                 20              250
100                                                 40
20
"""

numer_of_lines = int(input())
water_tank = 255
sum_liters = 0

for i in range (numer_of_lines):
    liters = int(input())
    if water_tank >= liters:
        water_tank -= liters
        sum_liters += liters
    else:
        print("Insufficient capacity!")
print(sum_liters)
