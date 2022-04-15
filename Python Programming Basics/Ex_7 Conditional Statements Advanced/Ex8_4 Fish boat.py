"""
Input               Output
3000                Not enough money! You need 570.00 leva.
Summer
11

3600                Not enough money! You need 180.00 leva.
Autumn
6

2000                Yes! You have 50.00 leva left.
Winter
13
"""
budget = int(input())
season = str(input())

if budget <= 100:
    place = "Bulgaria"
    if season = "Summer":
        type = "Camp"
        price = budget*0.3
    elif season = "Winter":
        type = "Hotel"
        price = budget*0.7
elif budget <= 1000:
    place = "Balkans"
    if season = "Summer":
        type = "Camp"
        price = budget*0.4
    elif season = "Winter":
        type = "Hotel"
        price = budget*0.8
elif budget > 1000:
    place = "Europe"
    type = "Hotel"
    price = budget*0.9

print(f"Somewhere in {place} ")
print(f"{type} - {price:.2f} ")
