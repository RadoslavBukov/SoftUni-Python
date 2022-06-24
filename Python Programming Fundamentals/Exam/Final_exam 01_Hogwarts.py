"""
Input	                        Output
A7ci0                           Done!
Illusion 1 c                    Done!
Illusion 4 o                    ACCIO
Abjuration
Abracadabra

TR1GG3R                         tr1gg3r
Necromancy                      The spell was too weak.
Illusion 8 m                    The spell was too weak.
Illusion 9 n
Abracadabra

SwordMaster                     The spell did not work!
Target Target Target            SWORDMASTER
Abjuration                      swordmaster
Necromancy                      sword
Alteration master
Abracadabra
"""
spell = input()
commands = input().split()

while commands[0] != "Abracadabra":
    if commands[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif commands[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif commands[0] == "Illusion":
        index = int(commands[1])
        letter = commands[2]
        if index < len(spell):
            spell = spell[0:index] + letter + spell[index+1:len(spell) + 1]
#            spell = spell.replace(spell[index], letter)
            print("Done!")
        else:
            print("The spell was too weak.")
    elif commands[0] == "Divination":
        first_substring = commands[1]
        second_substring = commands[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif commands[0] == "Alteration":
        substring = commands[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")
    commands = input().split()