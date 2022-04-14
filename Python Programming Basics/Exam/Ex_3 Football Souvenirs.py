"""
Input           Output
Brazil          Pepi bought 5 stickers of Brazil for 6.00 lv.
stickers
5

Denmark         Pepi bought 8 caps of Denmark for 52.00 lv.
caps
8

Croatia         Pepi bought 13 flags of Croatia for 35.75 lv.
flags
13

USA             Invalid country!
caps
18

Argentina       Invalid stock!
shirts
35
"""
team = str(input())
souvenir = str(input())
number_souvenir = int(input())

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25 * number_souvenir
    elif souvenir == "caps":
        price = 7.2 * number_souvenir
    elif souvenir == "posters":
        price = 5.1 * number_souvenir
    elif souvenir == "stickers":
        price = 1.25 * number_souvenir
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.2 * number_souvenir
    elif souvenir == "caps":
        price = 8.5 * number_souvenir
    elif souvenir == "posters":
        price = 5.35 * number_souvenir
    elif souvenir == "stickers":
        price = 1.2 * number_souvenir
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75 * number_souvenir
    elif souvenir == "caps":
        price = 6.9 * number_souvenir
    elif souvenir == "posters":
        price = 4.95 * number_souvenir
    elif souvenir == "stickers":
        price = 1.1 * number_souvenir
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.1 * number_souvenir
    elif souvenir == "caps":
        price = 6.5 * number_souvenir
    elif souvenir == "posters":
        price = 4.8 * number_souvenir
    elif souvenir == "stickers":
        price = 0.9 * number_souvenir

if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenir == "flags" or souvenir == "caps" or souvenir == "posters" or souvenir == "stickers":
        print(f"Pepi bought {number_souvenir} {souvenir} of {team} for {price:.2f} lv.")
    else:
        print(f"Invalid stock!")
else:
    print(f"Invalid country!")