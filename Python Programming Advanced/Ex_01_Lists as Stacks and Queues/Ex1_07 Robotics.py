"""
Input	                                Output
ROB-15;SS2-10;NX8000-3                  ROB - detail [08:00:01]
8:00:00                                 SS2 - glass [08:00:02]
detail                                  NX8000 - wood [08:00:03]
glass                                   NX8000 - apple [08:00:06]
wood
apple
End

ROB-8                                   ROB - detail [08:00:00]
7:59:59                                 ROB - wood [08:00:08]
detail                                  ROB - glass [08:00:16]
glass                                   ROB - sock [08:00:24]
wood
sock
End
"""
from collections import deque

# Function for adding robot name and time in dictionary {robot name: time}
def read_robots():
    result = {}
    robots_input = input().split(';')
    for i in robots_input:
        robots_info = i.split('-')
        name = robots_info[0]
        process_time = int(robots_info[1])
        result[name] = process_time
    return result

def to_seconds(hours, minutes, seconds):
    return hours*60*60 + minutes*60 + seconds

def read_products():
    result = deque()
    while True:
        line = input()
        if line == "End":
            break
        result.append(line)
    return result

def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) //60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

robots = read_robots()
available_robots = [x for x in robots.keys()]
busy_robots = {}

starting_time_parts = [int(x) for x in input().split(':')]
time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    for robot_name in [k for k in busy_robots.keys()]:
        busy_robots[robot_name] -= 1
        if busy_robots[robot_name] <= 0:
            busy_robots.pop(robot_name)
    concurrent_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in busy_robots:
            print(f"{robot_name} - {concurrent_product} [{to_str_time(time_in_seconds)}]")
            busy_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(concurrent_product)