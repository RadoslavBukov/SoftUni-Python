from Ex_01_project.person import Person

class Child(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

# its possible to write only "Pass" in the class, but this is more correct
# now we know that init is coming from Parent class and its require "name" and "age" parameters