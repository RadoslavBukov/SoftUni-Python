"""
Input	                Output
20.50                   You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.
1.25

15.75                   You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.
1.4
"""

budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = price_flour + (0.25 * price_flour)

price_loaves = price_flour + price_eggs + price_milk/4
loaves = 0
colored_eggs = 0

while budget-price_loaves > 0:
        loaves += 1
        budget -= price_loaves
        colored_eggs += 3
        if loaves % 3 == 0:
                colored_eggs -= loaves-2

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')