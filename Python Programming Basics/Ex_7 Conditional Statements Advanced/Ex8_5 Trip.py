"""
Input           Output
50              Somewhere in Bulgaria
summer	        Camp - 15.00

75              Somewhere in Bulgaria
winter	        Hotel - 52.50

312             Somewhere in Balkans
summer	        Camp - 124.80

678.53          Somewhere in Balkans
winter	        Hotel - 542.82

1500            Somewhere in Europe
summer	        Hotel - 1350.00
"""
budget = float(input())
season = str(input())

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        type = str("Camp")
        price = budget*0.3
    elif season == "winter":
        type = str("Hotel")
        price = budget*0.7
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        type = str("Camp")
        price = budget*0.4
    elif season == "winter":
        type = str("Hotel")
        price = budget*0.8
elif budget > 1000:
    place = "Europe"
    type = str("Hotel")
    price = budget*0.9

print(f"Somewhere in {place} ")
print(f"{type} - {price:.2f} ")
