"""
Input	                        Output	                            Comment
>>Sofa<<312.23!3                Bought furniture:                   Only the Sofa and the TV are valid, for each of them
>>TV<<300!5                     Sofa                                we multiply the price by the quantity and print the result
>Invalid<<!5                    TV
Purchase                        Total money spend: 2436.69
"""
import re

bought_items = list()
info = input()
total_price = 0

while info != "Purchase":

    pattern = r"(?P<name>(?<=>>)\w+)<<(?P<price>\d+(\.\d+)?(?=!))!(?P<quantity>\d+)"
    matches = re.finditer(pattern, info)

    for match in matches:
        name = match.group("name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        bought_items.append(name)
        total_price += (price*quantity)

    info = input()

print("Bought furniture:")
for i in bought_items:
    print(i)
print(f"Total money spend: {total_price:.2f}")