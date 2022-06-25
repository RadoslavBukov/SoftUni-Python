"""
Input	                                Output
Enroll Stefan                           Stefan is already enrolled.
Enroll Peter                            John doesn't exist.
Enroll Stefan                           George doesn't exist.
Learn Stefan ItShouldWork               Heroes:
Learn John ItShouldNotWork              == Stefan:
Unlearn George Dispel                   == Peter:
Unlearn Stefan ItShouldWork
End

Input	                                Output
Enroll Stefan                           Stefan has already learnt ItShouldWork.
Learn Stefan ItShouldWork               Stefan doesn't know NotFound.
Learn Stefan ItShouldWork               Heroes:
Unlearn Stefan NotFound                 == Stefan: ItShouldWork
End

Input	                                Output
Enroll Stefan                           End	Heroes:
Enroll Peter                            == Stefan: Spell
Enroll John                             == Peter: Dispel
Learn Stefan Spell                      == John:
Learn Peter Dispel
"""
command = input().split()
hero_dict = {}

while command[0] != "End":
    if command[0] == "Enroll":
        hero_name = command[1]
        if hero_name not in hero_dict.keys():
            hero_dict[hero_name] = list()
        else:
            print(f"{hero_name} is already enrolled.")
    if command[0] == "Learn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in hero_dict[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                hero_dict[hero_name].append(spell_name)
    if command[0] == "Unlearn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in hero_dict.keys():
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in hero_dict[hero_name]:
                hero_dict[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")

    command = input().split()
print(f"Heroes:")
for (key, value) in hero_dict.items():
    print(f"== {key}: ",end="")
    if len(value) > 0:
        print(", ".join(value))
    else:
        print("")