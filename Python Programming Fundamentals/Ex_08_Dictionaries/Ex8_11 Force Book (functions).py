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
def create_force_side(force_side, force_user, forces_dict):
    condition = [current_side for current_side in forces_dict if force_user in forces_dict[current_side]]
    if len(condition) == 0:
        condition.clear()
        if force_side not in forces_dict:
            forces_dict[force_side] = [force_user]
        else:
            forces_dict[force_side].append(force_user)
    return forces_dict

def create_force_user(force_user, force_side, forces_dict):
    for current_side in forces_dict:
        if force_user in forces_dict[current_side]:
            if len(forces_dict[current_side]) > 1:
                forces_dict[current_side].pop(force_user)
                break
            else:
                del forces_dict[current_side]
                break
    if force_side in forces_dict:
        forces_dict[force_side].append(force_user)
    else:
        forces_dict[force_side] = [force_user]
    print(f"{force_user} joins the {force_side} side!")

def force_book():
    forces_dict = {}
    while True:
        command = input()
        if command == 'Lumpawaroo':
            break
        if '|' in command:
            command = command.split(' | ')
            force_side = command[0]
            force_user = command[1]
            create_force_side(force_side, force_user, forces_dict)
        elif '->' in command:
            command = command.split(' -> ')
            force_user = command[0]
            force_side = command[1]
            create_force_user(force_user, force_side, forces_dict)
    for data in forces_dict:
        print(f'Side: {data}, Members: {len(forces_dict[data])}')
        for name in forces_dict[data]:
            print(f'! {name}')
force_book()