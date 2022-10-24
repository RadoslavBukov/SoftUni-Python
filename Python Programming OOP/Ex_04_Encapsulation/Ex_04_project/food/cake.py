from Ex_04_project.food.dessert import Dessert

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 100
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)

