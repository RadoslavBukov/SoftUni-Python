"""
Input           Output
2000            You saved the money for 2 days.
1000
spend
1200
save
2000

110             You can't save the money.
60              5
spend
10
spend
10
spend
10
spend
10
spend
10

250             You saved the money for 4 days.
150
spend
50
spend
50
save
100
save
100
"""
excursion_price = float(input())
budget = float(input())
spend = 0
all_days = 0
spend_days = 0

while budget < excursion_price:
    deistvie = input()
    pari = float(input())
    if deistvie == "spend":
        spend_days += 1
        all_days += 1
        budget -= pari
        if budget < 0:
            budget = 0
    elif deistvie == "save":
        spend_days = 0
        all_days += 1
        budget += pari
    if spend_days >= 5:
        print(f"You can't save the money.")
        print(f"{all_days}")
        break
if budget >= excursion_price:
    print(f"You saved the money for {all_days} days.")