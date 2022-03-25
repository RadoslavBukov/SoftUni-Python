"""
Input                   Output
Game of Thrones         You have enough time to watch Game of Thrones and left with 0 minutes free time.
60
96

Teen Wolf               You don't have enough time to watch Teen Wolf, you need 11 more minutes.
48
60
"""
from math import ceil
name = str(input())
episode_time = int(input())
rest_time = int(input())

lunch = rest_time/8
rest = rest_time/4

free_time = rest_time - lunch - rest

if episode_time > free_time:
    print(f"You don't have enough time to watch {name}, you need {ceil(episode_time-free_time)} more minutes.")
else:
    print(f'You have enough time to watch {name} and left with {ceil(free_time-episode_time)} minutes free time.')