"""
Input	                                                            Output
family 3 7210>>van 4 2345>>heavyDuty 9 31000>>sports 4 7410	        A family car will pay 59.00 euros in taxes.
                                                                    Invalid car type.
                                                                    A heavyDuty car will pay 50.00 euros in taxes.
                                                                    A sports car will pay 118.00 euros in taxes.
                                                                    The National Revenue Agency will collect 227.00 euros in taxes.
Comment
We start looping through the array, the first car is a family car, which should pay taxes for 3 years in use and has traveled 7210 km.
The taxes are calculate as follows: 7210 / 3000 * 12 + (50 - 3 * 5) = 59.00 euros
The family car must pay 59.00 euros in taxes.
The next car is a van, which is an invalid car type.
Next, we have heavyDuty car, with 9 years in use, and has traveled 31000 km. The tax which heavyDuty car should pay is 50.00 euros.
On the last iteration, we have a sports car that is 4 years in use and has traveled 7410 km. The tax which the sports car should pay is 118.00 euros.
At the end the National Revenue Agency collected 59.00 + 50.00 + 118.00 = 227.00 euros in taxes.

Input	                                                                                Output
family 5 3210>>pickUp 1 1345>>heavyDuty 7 21000>>sports 5 9410>>family 3 9012	        A family car will pay 37.00 euros in taxes.
                                                                                        Invalid car type.
                                                                                        A heavyDuty car will pay 52.00 euros in taxes.
                                                                                        A sports car will pay 127.00 euros in taxes.
                                                                                        A family car will pay 71.00 euros in taxes.
                                                                                        The National Revenue Agency will collect 287.00 euros in taxes.
"""
import math
vehicle_string = str(input())
vehicle_list = vehicle_string.split(">>")
initial_tax = 0
total_taxes = 0
valid_car = True

for i in range(len(vehicle_list)):
    car = vehicle_list[i].split(" ")
    car_type = str(car[0])
    years = int(car[1])
    kilometers = int(car[2])
    if car_type == "family":
        valid_car = True
        initial_tax = 50
        year_tax = 5
        increased_tax = 12
        taxes = (math.floor(kilometers / 3000)) * increased_tax + (initial_tax - years*year_tax)
    elif car_type == "heavyDuty":
        valid_car = True
        initial_tax = 80
        year_tax = 8
        increased_tax = 14
        taxes = (math.floor(kilometers / 9000)) * increased_tax + (initial_tax - years * year_tax)
    elif car_type == "sports":
        valid_car = True
        initial_tax = 100
        year_tax = 9
        increased_tax = 18
        taxes = (math.floor(kilometers / 2000)) * increased_tax + (initial_tax - (years * year_tax))
    else:
        valid_car = False
        print("Invalid car type.")
    if valid_car:
        print(f"A {car_type} car will pay {taxes:.2f} euros in taxes.")
        total_taxes += taxes
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")