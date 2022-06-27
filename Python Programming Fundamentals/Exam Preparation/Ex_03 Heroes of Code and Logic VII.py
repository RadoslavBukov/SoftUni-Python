"""
Input	                                    Output
2                                           Solmyr healed for 10 HP!
Solmyr 85 120                               Solmyr recharged for 50 MP!
Kyrre 99 50                                 Kyrre was hit for 66 HP by Orc and now has 33 HP left!
Heal - Solmyr - 10                          Kyrre has successfully cast ViewEarth and now has 35 MP!
Recharge - Solmyr - 50                      Solmyr
TakeDamage - Kyrre - 66 - Orc                 HP: 95
CastSpell - Kyrre - 15 - ViewEarth            MP: 170
End	                                        Kyrre
                                              HP: 33
                                              MP: 35

4                                           SirMullich healed for 30 HP!
Adela 90 150                                Adela recharged for 50 MP!
SirMullich 70 40                            Tyris does not have enough MP to cast Fireball!
Ivor 1 111                                  Tyris has been killed by Fireball!
Tyris 94 61                                 Ivor has been killed by Mosquito!
Heal - SirMullich - 50                      Adela
Recharge - Adela - 100                        HP: 90
CastSpell - Tyris - 1000 - Fireball           MP: 200
TakeDamage - Tyris - 99 - Fireball          SirMullich
TakeDamage - Ivor - 3 - Mosquito              HP: 100
End	                                          MP: 40
"""
n = int(input())
heroes = dict()
max_hp = 100
max_mp = 200

for i in range(0,n):
    heroes_input = input().split()
    hero_name = heroes_input[0]
    hit_points = heroes_input[1]
    mana_points = heroes_input[2]

    if hero_name not in heroes.keys():
        heroes[hero_name] = list()

    heroes[hero_name].append(int(hit_points))
    heroes[hero_name].append(int(mana_points))

pyrvi_elem = heroes[hero_name][0]
vtori_elem = heroes[hero_name][1]

commands = input().split(" - ")

while commands[0] != "End":
    if commands[0] == "CastSpell":
        hero_name = commands[1]
        MP_needed = int(commands[2])
        spell_name = commands[3]
        if int(heroes[hero_name][1]) >= MP_needed:
            heroes[hero_name][1] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif commands[0] == "TakeDamage":
        hero_name = commands[1]
        damage = int(commands[2])
        attacker = commands[3]
        if heroes[hero_name][0] > damage:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif commands[0] == "Recharge":
        hero_name = commands[1]
        amount = int(commands[2])
        initial_mana = heroes[hero_name][1]
        heroes[hero_name][1] += amount
        if heroes[hero_name][1] > max_mp:
            amount = max_mp - initial_mana
            heroes[hero_name][1] = max_mp
        print(f"{hero_name} recharged for {amount} MP!")
    elif commands[0] == "Heal":
        hero_name = commands[1]
        amount = int(commands[2])
        initial_heal = heroes[hero_name][0]
        heroes[hero_name][0] += amount
        if heroes[hero_name][0] > max_hp:
            amount = max_hp - initial_heal
            heroes[hero_name][0] = max_hp
        print(f"{hero_name} healed for {amount} HP!")
    commands = input().split(" - ")

for (key, value) in heroes.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")