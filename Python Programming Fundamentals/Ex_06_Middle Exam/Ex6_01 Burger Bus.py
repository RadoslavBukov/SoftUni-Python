"""
Input	                        Output
3                               In Sofia Burger Bus earned 682.17 leva.
Sofia                           In Plovdiv Burger Bus earned 1672.94 leva.
895.67                          In Burgas Burger Bus earned 1460.55 leva.
213.50                          Burger Bus total profit: 3815.66 leva.
Plovdiv
2563.20
890.26
Burgas
2360.55
600.00

Input	                        Output
5                               In Lille Burger Bus earned 1025.40 leva.
Lille                           In Rennes Burger Bus earned 860.40 leva.
2226.00                         In Reims Burger Bus earned -78.28 leva.
1200.60                         In Bordeaux Burger Bus earned 4274.90 leva.
Rennes                          In Montpellier Burger Bus earned 322.25 leva.
6320.60                         Burger Bus total profit: 6404.67 leva.
5460.20
Reims
600.20
452.32
Bordeaux
6925.30
2650.40
Montpellier
680.50
290.20
"""
number_cities = int(input())
total_profit = 0

for i in range(1, number_cities+1):
    city_name = str(input())
    earned_money = float(input())
    expenses = float(input())
    if i % 3 == 0 and i % 5 != 0:
        expenses += expenses*0.5
    if i % 5 == 0:
        earned_money -= earned_money*0.1
    city_profit = earned_money - expenses
    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")
    total_profit += city_profit
print(f"Burger Bus total profit: {total_profit:.2f} leva.")