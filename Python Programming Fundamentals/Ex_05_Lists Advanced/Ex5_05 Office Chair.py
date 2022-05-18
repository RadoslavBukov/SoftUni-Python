"""
Input	                Output
4                       Game On, 4 free chairs left
XXXX 4
XX 1
XXXXXX 3
XXX 3

3                       1 more chairs needed in room 2
XXXXXXX 5               2 more chairs needed in room 3
XXXX 5
XXXXXX 8
"""

rooms = int(input())
free_chair = 0
game_on = True

for i in range (1, rooms+1):
    input_list = input().split(" ")
    chairs = len(input_list[0])
    visitors = int(input_list[1])
    if visitors > chairs:
        print(f"{visitors-chairs} more chairs needed in room {i}")
        game_on = False
    else:
        free_chair += chairs-visitors

if game_on:
    print(f"Game On, {free_chair} free chairs left")