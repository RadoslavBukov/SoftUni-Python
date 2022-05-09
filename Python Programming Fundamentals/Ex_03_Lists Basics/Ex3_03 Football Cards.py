"""
Input	                                Output
A-1 A-5 A-10 B-2	                    Team A - 8; Team B - 10

A-1 A-5 A-10 B-2 A-10 A-7 A-3	        Team A - 6; Team B - 10
                                        Game was terminated
"""

text = str(input())
text_list = text.split(" ")
set = set(text_list)
list2 = list(set)

players_A = 0
players_B = 0
terminate = False

for element in list2:
    if "A" in element:
        players_A += 1
    elif "B" in element:
        players_B += 1
    if players_A > 4 or players_B > 4:
        terminate = True
        break
print(f"Team A - {11-players_A}; Team B - {11-players_B}")
if terminate:
    print("Game was terminated")
