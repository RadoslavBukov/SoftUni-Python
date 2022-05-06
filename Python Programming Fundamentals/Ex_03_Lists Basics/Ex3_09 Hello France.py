"""
Input	                                                                                    Output
Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60                60.62 35.35 51.13
120	                                                                                        Profit: 42.03
                                                                                            Hello, France!

Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60        28.42 21.84 46.62
90                                                                                          Profit: 27.68
                                                                                            Not enough money.
"""
money=150
clothes_max=50
shoes_max=35
accessories_max=20.5
items = str(input())
list_items = items.split("|")
budget = float(input())
list_price = []
type_item=0
price_item=0
sell_product=0
sum_price=0

for i in range(len(list_items)):
    list_price = list_items[i].split("->")
    type_item = list_price[0]
    price_item = float(list_price[1])
    if price_item<=budget and ((type_item == "Clothes" and price_item<=clothes_max) or (type_item == "Shoes" and price_item<=shoes_max) or (type_item == "Accessories" and price_item<=accessories_max)):
        new_price = 0
        budget -= price_item
        sum_price += price_item
        new_price += price_item+(price_item*0.4)
        sell_product += new_price
        print(f"{new_price:.2f}",end=" ")
print(f"\nProfit: {(sell_product-sum_price):.2f}")

if sell_product+budget >= money:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")