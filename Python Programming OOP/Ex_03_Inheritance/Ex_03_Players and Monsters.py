"""
Test Code	                                                Output
hero = Hero("H", 4)                                         H
print(hero.username)                                        4
print(hero.level)                                           H of type Hero has level 4
print(str(hero))                                            E of type Elf has level 4
elf = Elf("E", 4)                                           Hero
print(str(elf))                                             E
print(elf.__class__.__bases__[0].__name__)                  4
print(elf.username)
print(elf.level)
"""


from Ex_03_project.hero import Hero
from Ex_03_project.elf import Elf
from Ex_03_project.blade_knight import BladeKnight
from Ex_03_project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
blade = BladeKnight("BK", 4)
print(hero.username)
print(hero.level)
print(str(hero))
soul = SoulMaster("BK", 4)
print(hero.username)
print(hero.level)
print(str(hero))
