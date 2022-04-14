"""
Input           Output
3.5             The spacecraft holds 8 astronauts.
4
5
1.70

4.5             The spacecraft is too big.
4.8
5
1.75

3               The spacecraft holds 4 astronauts.
3
4
1.68
"""
import math
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_astronaut_height = float(input())

ship_capacity = ship_width*ship_length*ship_height
room_capacity = (average_astronaut_height+0.4)*2*2
astronaut_number = ship_capacity/room_capacity

if astronaut_number < 3:
    print(f"The spacecraft is too small.")
elif 3 <= astronaut_number <= 10:
    print(f"The spacecraft holds {math.floor(astronaut_number)} astronauts.")
else:
    print(f"The spacecraft is too big.")