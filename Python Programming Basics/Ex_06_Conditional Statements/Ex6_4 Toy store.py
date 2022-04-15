"""
Input	    Output
40.8        Yes! 418.20 lv left.
20
25
30
50
10

320         Not enough money! 238.73 lv needed.
8
2
5
5
1
"""
puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2
excursion = float(input())
number_puzzles = float(input())
number_dolls = float(input())
number_bears = float(input())
number_minions = float(input())
number_trucks = float(input())

sum = number_puzzles*puzzle + number_dolls*doll + number_bears*bear + number_minions*minion + number_trucks*truck
toy_number = number_puzzles + number_dolls + number_bears + number_trucks + number_minions
if toy_number >= 50:
    discount = sum*0.25
    final_price = sum - discount
else:
    final_price = sum
rent = final_price * 0.1
profit = final_price - rent

if profit >= excursion:
    difference = profit-excursion
    print(f'Yes! {difference:.2f} lv left.')
else:
    difference = excursion-profit
    print(f'Not enough money! {difference:.2f} lv needed.')