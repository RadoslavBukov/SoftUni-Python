"""
Input                       Output
14                          264.06
apartment
positive

30                          730.80
president apartment
negative

12                          247.50
room for one person
positive

2                           21.88
apartment
positive
"""
days = int(input())
type = str(input())
rating = str(input())

room = 18
apartment = 25
president = 35

price = (days-1)*room
if type == "apartment":
    price = (days - 1) * apartment
    if days < 11:
        price -= price * 0.3
    elif 11 <= days <= 16:
        price -= price * 0.35
    elif days > 16:
        price -= price * 0.50
elif type == "president apartment":
    price = (days - 1) * president
    if days < 11:
        price -= price * 0.1
    elif 11 <= days <= 16:
        price -= price * 0.15
    elif days > 16:
        price -= price * 0.2

if rating == "positive":
    price += price*0.25
elif rating == "negative":
    price -= price*0.1

print(f"{price:.2f}")
