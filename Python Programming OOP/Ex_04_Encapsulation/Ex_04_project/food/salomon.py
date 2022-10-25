from Ex_04_project.food.main_dish import MainDish


class Salomon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)