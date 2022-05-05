"""
Input	                                                                    Output
Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes                  StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg
OutOfStock Eggs
Required Spoon 2
JustInCase ChocolateEgg
No Money

Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes                    Sweets Cozonac Chocolate Flowers Wine
Required Paper 8                                                            Eggs Hat
OutOfStock Clothes
Required Chocolate 2
JustInCase Hat
OutOfStock Cable
No Money
"""

gifts = str(input())
gifts_list = gifts.split(" ")
command = ""
index = 0

while command != "No Money":
    command_list = command.split(" ")
    if "OutOfStock" in command_list:
        for i in range(len(gifts_list)):
            if command_list[1] == gifts_list[i]:
                gifts_list[i] = "None"
    if "Required" in command_list:
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_list[1]
    if "JustInCase" in command_list:
        gifts_list[-1] = command_list[1]
    command = str(input())
while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep=" ")