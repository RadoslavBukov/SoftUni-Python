from Ex_04_project.product import Product

class Beverage(Product):

#   variable milliliters is additional to clas Beverage, se we add it in __init_:
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters