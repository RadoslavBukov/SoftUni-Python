"""
#Before	                                                        Result
shapes = [Rectangle(2, 3), Rectangle(1, 6)]                     The total area is:  12
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

#After	                                                        Result
shapes = [Rectangle(1, 6), Triangle(2, 3)]                      The total area is:  9.0
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
"""
# SRP (Single Responsibility Principle): Each class is responsible for only one thing and should have only one reason to change
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calc_area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return (self.width * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total

# Before
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)

# After
shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
