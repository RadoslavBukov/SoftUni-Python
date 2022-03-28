"""
Input           Output
16              It's 16 degrees, get your Sweatshirt and Sneakers.
Morning

22              It's 22 degrees, get your T-Shirt and Sandals.
Afternoon

28              It's 28 degrees, get your Shirt and Moccasins.
Evening
"""
from math import ceil

degrees = int(input())
day_time = str(input())

if day_time == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif day_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
