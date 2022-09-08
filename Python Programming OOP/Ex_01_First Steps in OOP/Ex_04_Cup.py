"""
Test Code	                    Output
cup = Cup(100, 50)              50
print(cup.status())             10
cup.fill(40)
cup.fill(20)
print(cup.status())
"""
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, increase_quantity):
        if self.status() >= increase_quantity:
            self.quantity += increase_quantity

    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
