"""
Input           Output
10464           No, he failed! He was 20786.00 seconds slower.
1500
20

55555.67        Yes, he succeeded! The new world record is 17688.01 seconds.
3017
5.03
"""
from math import floor

record = float(input())
distance = float(input())
first_place_time = float(input())

slow_down = floor(distance/15) * 12.5

ivan_time = distance * first_place_time + slow_down

if record <= ivan_time:
    print(f'No, he failed! He was {ivan_time-record:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')