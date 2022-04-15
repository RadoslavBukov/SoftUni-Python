"""
Input           Output
6               Group 1: 2 cats.
102             Group 2: 2 cats.
236             Group 3: 2 cats.
123             Price for food per day: 17.73 lv.
399
342
222

10              Group 1: 3 cats.
256             Group 2: 3 cats.
348             Group 3: 4 cats.
198             Price for food per day: 31.44 lv.
322
186
294
321
100
200
300

7               Group 1: 2 cats.
100             Group 2: 3 cats.
200             Group 3: 2 cats.
342             Price for food per day: 18.81 lv.
300
234
123
212
"""
number_cats = int(input())
price_1kg = 12.45
group_1 = 0
group_2 = 0
group_3 = 0
all_food_grams = 0

for i in range (0, number_cats):
    food_grams = float(input())
    if 100 <= food_grams < 200:
        group_1 += 1
    elif 200 <= food_grams < 300:
        group_2 += 1
    elif 300 <= food_grams < 400:
        group_3 += 1
    all_food_grams += food_grams

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {((all_food_grams/1000) * price_1kg):.2f} lv.")