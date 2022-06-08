"""
Input	                    Output	                                    Comments

Light | Peter               Side: Light, Members: 1                     We register Peter on the Light side and Kim on the Dark side.
Dark | Kim                  ! Peter                                     After receiving "Lumpawaroo", we print both sides.
Light | Kim                 Side: Dark, Members: 1
Lumpawaroo	                ! Kim

Lighter | Royal             Ivan Ivanov joins the Lighter side!         Although Ivan Ivanov doesn't have a profile, we register him and add him to the Lighter side.
Darker | DCay               DCay joins the Lighter side!                We remove DCay from the Darker side and add him to the Lighter side.
Ivan Ivanov -> Lighter      Side: Lighter, Members: 3                   We print only the Lighter side because the Darker side has no members.
DCay -> Lighter             ! Royal
Lumpawaroo	                ! Ivan Ivanov
                            ! DCay
"""
text = input()
forces_dict = dict()
name_exist = False

while 'Lumpawaroo' not in text:
    name_exist = False
    if "|" in text:
        text = text.split(" | ")
        force_side = text[0]
        force_user = text[1]
        if force_side not in forces_dict.keys():            # Check if Forse side is a key from the dictionary
            forces_dict[force_side] = list()                # If not -> Add a key(force_side) with value = list() to forces_dict dictionary
        for values in forces_dict.values():                 # Check if force user exist in all values(values are lists)
            if force_user in values:
                name_exist = True
        if not name_exist:
            forces_dict[force_side].append(force_user)
    elif "->" in text:
        text = text.split(" -> ")
        force_side = text[1]
        force_user = text[0]
        for (key,value) in forces_dict.items():
            if force_user in value:                         # Check if force user exist in all values(values are lists)
                if len(value) > 1:
                    forces_dict[force_side].pop(force_user)     # Remove the element = force user, from the list (list is a value of the key)
                else:
                    del forces_dict[key]                        # If only 1 member with this name is in values(list) del the entire key.
                    break
        if force_side not in forces_dict.keys():                # Check if forse side exist
            forces_dict[force_side] = list()
            if force_user not in forces_dict.values():          # Check if the user exist in the key - value (list)
                forces_dict[force_side].append(force_user)
        else:
            forces_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    text = input()

for (key, value) in forces_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for names in (value):
            print(f"! {names}")