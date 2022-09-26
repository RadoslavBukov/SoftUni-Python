"""
Test Code	                                                Output
vehicle = Vehicle(50, 150)                                  1.25
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)                     3
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)                   50
print(vehicle.fuel)                                         150
print(vehicle.horse_power)                                  1.25
print(vehicle.fuel_consumption)                             50
vehicle.drive(100)                                          0
print(vehicle.fuel)                                         0
family_car = FamilyCar(150, 150)                            Car
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
"""
from Ex_04_project.vehicle import Vehicle
from Ex_04_project.car import Car
from Ex_04_project.motorcycle import Motorcycle
from Ex_04_project.cross_motorcycle import CrossMotorcycle
from Ex_04_project.race_motorcycle import RaceMotorcycle
from Ex_04_project.family_car import FamilyCar



vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
