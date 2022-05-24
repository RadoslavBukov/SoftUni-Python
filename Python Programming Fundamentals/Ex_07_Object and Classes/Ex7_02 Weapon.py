"""
Test Code	                            Output
weapon = Weapon(5)                      shooting...
print(weapon.shoot())                   shooting...
print(weapon.shoot())                   Remaining bullets: 3
print(weapon)                           shooting...
print(weapon.shoot())                   shooting...
print(weapon.shoot())                   shooting...
print(weapon.shoot())                   no bullets left
print(weapon.shoot())                   Remaining bullets: 0
print(weapon)
"""
class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)