from Ex_04_project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
# MILLILITERS and PRICE are constant variable for class Coffee
    MILLILITERS = 50
    PRICE = 3.50

# in __init__ method we are getting only name and caffeine(private attribute for class Coffee), because PRICE and MILLILITERS are constant for this class.
    def __init__(self, name, caffeine): # Getting only name and caffeine
        super().__init__(name, self.PRICE, self.MILLILITERS)    # name from Parents class
        self.__caffeine = caffeine  # caffeine from Coffee instances initialisation

#   Getter for private caffeine variable:
    @property
    def caffeine(self):
        return self.__caffeine

