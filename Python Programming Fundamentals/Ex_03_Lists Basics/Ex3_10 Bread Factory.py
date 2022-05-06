"""
Input	                                                                Output
rest-2|order-10|eggs-100|rest-10 	                                    You gained 0 energy.
                                                                        Current energy: 100.
                                                                        You earned 10 coins.
                                                                        You bought eggs.
                                                                        You gained 10 energy.
                                                                        Current energy: 80.
                                                                        Day completed!
                                                                        Coins: 10
                                                                        Energy: 80
order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
"""
energy = 100
coins = 100
events = str(input())
list_events=events.split("|")
list_ev_num=[]
type_event=''
number=0
new_energy=0
day_stoped=False

for i in range (len(list_events)):
    energy_diff = 0
    list_ev_num = list_events[i].split("-")
    type_event = list_ev_num[0]
    number = int(list_ev_num[1])
    if type_event == "rest":
        new_energy = energy+number
        if new_energy >= 100:
            new_energy = 100
        energy_diff = new_energy-energy
        energy = new_energy
        print(f"You gained {energy_diff} energy.")
        print(f"Current energy: {energy}.")
    if type_event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    elif type_event != "rest" and type_event != "order":
        if coins >= number:
            coins -= number
            print(f"You bought {type_event}.")
        else:
            print(f"Closed! Cannot afford {type_event}.")
            day_stoped=True
            break
if not day_stoped:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")