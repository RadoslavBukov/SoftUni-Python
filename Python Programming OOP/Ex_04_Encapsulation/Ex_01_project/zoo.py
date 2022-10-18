from Ex_01_project.animal import Animal
from Ex_01_project.caretaker import Caretaker
from Ex_01_project.cheetah import Cheetah
from Ex_01_project.keeper import Keeper
from Ex_01_project.lion import Lion
from Ex_01_project.tiger import Tiger
from Ex_01_project.vet import Vet
from Ex_01_project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return f"Not enough space for animal"
        if price > self.__budget:
            return f"Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tends = 0
        for animal in self.animals:
            tends += animal.money_for_care
        if tends > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy"
        self.__budget -= tends
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        caretaker = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        result += f"----- {len(caretaker)} Caretakers:\n" + '\n'.join(caretaker) + '\n'
        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return result