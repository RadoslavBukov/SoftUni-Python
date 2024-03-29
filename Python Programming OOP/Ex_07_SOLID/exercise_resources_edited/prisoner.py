"""
#Before	                                                                        Result
prisoner = Prisoner()                                                           The prisoner trying to walk to north by 10 and east by -3.
print("The prisoner trying to walk to north by 10 and east by -3.")             The location of the prison: [3, 3]
                                                                                The current position of the prisoner: [0, 13]
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

#After	                                                                        Result
prisoner = Prisoner()                                                           The prisoner trying to walk to north by 10 and east by -3.
print("The prisoner trying to walk to north by 10 and east by -3.")             The location of the prison: (3, 3)
                                                                                The current position of the prisoner: (3, 3)
try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")
"""
# LSP (Liskov Substitution Principle) - Every child class behavior should be same as his parents class behavior
import copy

class Person:

    def __init__(self, position):
        self.position = position

class FreePerson(Person):

    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))

# Before
prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")