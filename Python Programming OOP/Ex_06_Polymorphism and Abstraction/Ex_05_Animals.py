"""
Output Test Code 1:
Woof!
This is Rocky. Rocky is a 3 year old Male Dog
Hiss
This is Tom. Tom is a 6 year old Male Tomcat

Output Test Code 2:
Meow
This is Kiki. Kiki is a 1 year old Female Kitten
Meow meow!
This is Johnny. Johnny is a 7 year old Male Cat
"""
from Ex_05_project.animal import Animal
from Ex_05_project.cat import Cat
from Ex_05_project.dog import Dog
from Ex_05_project.kitten import Kitten
from Ex_05_project.tomcat import Tomcat

# Test Code 1
dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)


# Test Code 2
# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)
# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)