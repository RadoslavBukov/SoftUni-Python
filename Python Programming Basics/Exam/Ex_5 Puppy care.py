"""
Input           Output
4               Food is enough! Leftovers: 2595 grams.
130
345
400
180
230
120
Adopted

3               Food is enough! Leftovers: 0 grams.
1000
1000
1000
Adopted

2               Food is not enough. You need 2032 grams more.
999
456
999
999
"""
all_dog_food = (int(input())*1000)
grams_per_serve = input()
sum_eaten_food = 0

while grams_per_serve != "Adopted":
    sum_eaten_food += int(grams_per_serve)
    grams_per_serve = input()

if all_dog_food >= sum_eaten_food:
    print(f"Food is enough! Leftovers: {all_dog_food-sum_eaten_food} grams.")
else:
    print(f"Food is not enough. You need {sum_eaten_food-all_dog_food} grams more.")
