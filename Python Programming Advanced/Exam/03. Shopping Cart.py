"""
Test Code	                                Output
print(shopping_cart(                        Pizza:
    ('Pizza', 'ham'),                        - cheese
    ('Soup', 'carrots'),                     - flour
    ('Pizza', 'cheese'),                     - ham
    ('Pizza', 'flour'),                      - mushrooms
    ('Dessert', 'milk'),                    Dessert:
    ('Pizza', 'mushrooms'),                  - milk
    ('Pizza', 'tomatoes'),                  Soup:
    'Stop',                                  - carrots
))

print(shopping_cart(                        Dessert:
    ('Pizza', 'ham'),                        - milk
    ('Dessert', 'milk'),                    Pizza:
    ('Pizza', 'ham'),                        - ham
    'Stop',                                 Soup:
))

print(shopping_cart(                        No products in the cart!
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))	
"""
def shopping_cart(*args):
    limit_dict = {
        "Soup" : 3,
        "Pizza" : 4,
        "Dessert" : 2,
    }

    meals_products = {"Soup": [], "Pizza": [], "Dessert": []}
    for tuple in args:
        if tuple != "Stop":
            meal, product = tuple
            if (len(meals_products[meal]) < limit_dict[meal]) and (product not in meals_products[meal]):
                meals_products[meal].append(product)
        else:
            break

    sorted_meals = sorted(meals_products.items(), key=lambda x: (-len(x[1]), x[0]))

    if any(a != [] for a in meals_products.values()):
        result = []
        for key, value in sorted_meals:
            result.append(f"{key}:")
            for el in sorted(value):
                result.append(f" - {el}")
        return "\n".join(result)
    else:
        return f"No products in the cart!"

# Test Code 1
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# Test Code 2
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# Test Code 3
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))