"""
Test Code	                                                Output
peter = Vet("Peter")                                        Tom registered in the clinic
george = Vet("George")                                      Cory registered in the clinic
print(peter.register_animal("Tom"))                         Fishy registered in the clinic
print(george.register_animal("Cory"))                       Bobby registered in the clinic
print(peter.register_animal("Fishy"))                       Kay registered in the clinic
print(peter.register_animal("Bobby"))                       Cory unregistered successfully
print(george.register_animal("Kay"))                        Silky registered in the clinic
print(george.unregister_animal("Cory"))                     Molly not in the clinic
print(peter.register_animal("Silky"))                       Tom unregistered successfully
print(peter.unregister_animal("Molly"))                     Peter has 3 animals. 1 space left in clinic
print(peter.unregister_animal("Tom"))                       George has 1 animals. 1 space left in clinic
print(peter.info())
print(george.info())
"""
class Vet:

    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self,animal):
        if len(self.animals) >= Vet.space:
            return "Not enough space"
        self.animals.append(animal)
        Vet.animals.append(animal)
        return f"{animal} registered in the clinic"

    def unregister_animal(self,animal):
        if animal not in self.animals:
            return f"{animal} not in the clinic"
        self.animals.remove(animal)
        Vet.animals.remove(animal)
        return f"{animal} unregistered successfully"

    def info(self):
        return f"{self.vet_name} has {len(self.animals)} animals. {Vet.space-len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
