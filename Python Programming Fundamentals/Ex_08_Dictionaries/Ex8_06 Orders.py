"""
Input	                            Output
Beer 2.20 100                       buy	Beer -> 220.00
IceTea 1.50 50                      IceTea -> 75.00
NukaCola 3.30 80                    NukaCola -> 264.00
Water 1.00 500                      Water -> 500.00

Beer 2.40 350                       buy	Beer -> 660.00
Water 1.25 200                      Water -> 250.00
IceTea 5.20 100                     IceTea -> 110.00
Beer 1.20 200
IceTea 0.50 120

CesarSalad 10.20 25                 buy	CesarSalad -> 255.00
SuperEnergy 0.80 400                SuperEnergy -> 320.00
Beer 1.35 350                       Beer -> 472.50
IceCream 1.50 25                    IceCream -> 37.50
"""
def multiplyList(xList):
    product = 1
    for x in xList:
        product = product * x
    return product

product = input().split(" ")
orders = dict()

while product[0] != "buy":
    name = product[0]
    price = float(product[1])
    quantity = int(product[2])

    if name not in orders.keys():
        orders[name] = list()
        orders[name].append(price)
        orders[name].append(quantity)
    else:
        orders[name][0] = price
        orders[name][1] += quantity
    product = input().split(" ")

for (key,value) in orders.items():
    print(f"{key} -> {multiplyList(value):.2f}")