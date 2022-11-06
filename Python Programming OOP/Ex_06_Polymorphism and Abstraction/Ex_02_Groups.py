"""
Test Code	                                                Output
p0 = Person('Aliko', 'Dangote')                             3
p1 = Person('Bill', 'Gates')                                Group Special with members Elon Musk, Warren Musk
p2 = Person('Warren', 'Buffet')                             Person 0: Aliko Dangote
p3 = Person('Elon', 'Musk')                                 Person 0: Aliko Dangote
p4 = p2 + p3                                                Person 1: Bill Gates
                                                            Person 2: Warren Buffet
first_group = Group('__VIP__', [p0, p1, p2])                Person 3: Elon Musk
second_group = Group('Special', [p3, p4])                   Person 4: Warren Musk
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
"""
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        people = self.people + other.people
        return Group(new_name, people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

# For itteration in list of objects
    def __getitem__(self, idx):
        return f"Person {idx}: {str(self.people[idx])}"

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
