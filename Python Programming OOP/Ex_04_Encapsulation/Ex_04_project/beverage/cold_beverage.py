from Ex_04_project.beverage.beverage import Beverage


class ColdBaverage(Beverage):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)