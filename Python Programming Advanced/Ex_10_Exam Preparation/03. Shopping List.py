"""
Test Code	                                            Output
print(shopping_list(100,                                You bought skirts for 60.00 leva.
                    microwave=(70, 2),                  You bought coffee for 15.00 leva.
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,                                 You do not have enough budget.
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,                                You bought cola for 2.40 leva.
                    cola=(1.20, 2),                     You bought candies for 3.75 leva.
                    candies=(0.25, 15),                 You bought bread for 1.80 leva.
                    bread=(1.80, 1),                    You bought pie for 52.50 leva.
                    pie=(10.50, 5),                     You bought tomatoes for 4.20 leva.
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
"""
def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    basket_products = 0

    result = ""
    new_dict = {}
    for key, val in kwargs.items():
        new_dict[key] = val

    while basket_products < 5 and kwargs:
        for item, value in new_dict.items():
            price, quantity = value
            if basket_products >= 5:
                break
            if budget > price*quantity:
                budget -= price*quantity
                basket_products += 1
                result += (f"You bought {item} for {price*quantity:.2f} leva.\n")
            kwargs.pop(item)
    return result


# Test Code 1
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# Test Code 2
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# Test Code 3
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))