"""
Input	            Output
10                  Everyone is safe.
5                   3 total cars passed the crossroads.
Mercedes
green
Mercedes
BMW
Skoda
green
END

9                   A crash happend!
3                   Hummer was hit at e.
Mercedes
Hummer
green
Hummer
Mercedes
green
END
"""
from collections import deque

def car_name_q(name):
    car_name_queue = deque()
    for ch in name:
        car_name_queue.append(ch)
    return car_name_queue


green_light_duration = int(input())
free_window_duration = int(input())
total_cars_passed = 0
cars = deque()
time = green_light_duration
crash = False

command = input()
while command != "END":
    if command != 'green':
        cars.append(command)
    else:
        time = green_light_duration
        while time > 0 and cars:
            car = cars.popleft()
            car_name = car_name_q(car)
            while car_name:
                if time > 0:
                    time -= 1
                    car_name.popleft()
                    if not car_name and time >= 0:
                        total_cars_passed += 1
                else:
                    if len(car_name) > free_window_duration:
                        for _ in range(free_window_duration):
                            car_name.popleft()
                        crash = True
                        print(f"A crash happened!")
                        print(f"{car} was hit at {car_name[0]}.")
                    else:
                        total_cars_passed += 1
                    break
    if not crash:
        command = input()
    else:
        break
if not crash:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')