"""
Input	        Output
3               1
1 5
10 3
3 4

5               0
22 5
14 10
52 7
21 12
36 9
"""
from collections import deque

number_petrol_pumps = int(input())
pumps = deque()

for _ in range(number_petrol_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(number_petrol_pumps):
    truck_tank = 0
    failed = False
    for petrol, distance in pumps:
        truck_tank = truck_tank + petrol - distance
        if truck_tank < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break