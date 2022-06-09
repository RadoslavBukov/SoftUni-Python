"""
Input	    Output
Gold        Gold -> 155
155         Silver -> 10
Silver      Copper -> 17
10
Copper
17
stop

gold        gold -> 170
155         silver -> 10
silver      copper -> 17
10
copper
17
gold
15
stop
"""
text = input()
dictionary = dict()

while text != "stop":
    quantity = int(input())
    if text not in dictionary.keys():
        dictionary[text] = quantity
    else:
        dictionary[text] += quantity
    text = input()

for (key,value) in dictionary.items():
    print(f"{key} -> {value}")

"""
# 2nd Solution

def miner_task():
    dictionary = {}
    
    while True:
        resource = input()
        if resource == "stop":
            break    
        quantity = int(input())
        if resource not in items:
            dictionary[resource] = quantity
        else:
            dictionary[resource] += quantity
            
    for (key,value) in dictionary.items():
    print(f"{key} -> {value}")
"""