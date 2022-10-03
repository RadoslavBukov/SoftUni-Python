from Ex_02_project.animal import Animal


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)