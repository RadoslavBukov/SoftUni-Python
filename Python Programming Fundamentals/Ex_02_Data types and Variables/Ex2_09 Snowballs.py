"""
Input	    Output                      Input       Output
2           10 : 2 = 125 (3)            3           10 : 5 = 128 (7)
10                                      10
2                                       5
3                                       7
5                                       16
5                                       4
5	                                    2
                                        20
                                        2
                                        2
"""

snowballs_number = int(input())
best_value = 0

for i in range (snowballs_number):
    weight = int(input())
    time_fly = int(input())
    quality = int(input())
    value = (weight//time_fly)**quality
    if value > best_value:
        best_weight = weight
        best_time = time_fly
        best_quality = quality
        best_value = value
print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")