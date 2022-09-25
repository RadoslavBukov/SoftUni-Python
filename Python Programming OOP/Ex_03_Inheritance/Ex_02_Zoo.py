"""
Test Code	                                                    Output
mammal = Mammal("Stella")                                       Animal
print(mammal.__class__.__bases__[0].__name__)                   Stella
print(mammal.name)                                              Reptile
lizard = Lizard("John")                                         John
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
"""
from Ex_02_project.animal import Animal
from Ex_02_project.reptile import Reptile
from Ex_02_project.mammal import Mammal
from Ex_02_project.lizard import Lizard
from Ex_02_project.snake import Snake
from Ex_02_project.gorilla import Gorilla
from Ex_02_project.bear import Bear


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
