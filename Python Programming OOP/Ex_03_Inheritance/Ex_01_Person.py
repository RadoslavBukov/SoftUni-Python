"""
Test Code	                                        Output
person = Person("Peter", 25)                        Peter
child = Child("Peter Junior", 5)                    25
print(person.name)                                  Person
print(person.age)
print(child.__class__.__bases__[0].__name__)
"""
from Ex_01_project.person import Person
from Ex_01_project.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
