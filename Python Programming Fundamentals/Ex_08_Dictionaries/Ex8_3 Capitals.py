"""
Input	                                        Output
Bulgaria, Romania, Germany, England             Bulgaria -> Sofia
Sofia, Bucharest, Berlin, London	            Romania -> Bucharest
                                                Germany -> Berlin
                                                England -> London
Bulgaria, Germany, France                       Bulgaria -> Varna
Varna, Frankfurt, Paris	                        Germany -> Frankfurt
                                                France -> Paris
"""
countries = input().split(", ")
capitals = input().split(", ")
dictionary = {countries[i]:capitals[i] for i in range(0,len(countries))}

for (key,value) in dictionary.items():
    print(f"{key} -> {value}")

"""
# 2nd solution with function

def capitals():
    countries = input().split(", ")
    capitals = input().split(", ")
    result = dict(zip(countries, capitals))         #From two lists we create a dict with tuples
    
    for (key,value) in dictionary.items():
        print(f"{key} -> {value}") 

capitals()
"""