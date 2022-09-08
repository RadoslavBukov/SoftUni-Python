"""
Test Code	                        Output
hero = Hero("Peter", 100)           None
print(hero.defend(50))              None
hero.heal(50)                       Peter was defeated
print(hero.defend(99))
print(hero.defend(1))
"""
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self,damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self,amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
