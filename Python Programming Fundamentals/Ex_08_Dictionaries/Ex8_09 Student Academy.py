"""
Input	                Output
5                       John -> 5.00
John                    Alice -> 4.50
5.5                     George -> 5.00
John
4.5
Alice
6
Alice
3
George
5

5                       Rob -> 5.50
Amanda                  Christian -> 5.00
3.5                     Robert -> 6.00
Amanda
4
Rob
5.5
Christian
5
Robert
6
"""
rows = int(input())
dictionary = dict()

for i in range(rows):
    name = input()
    grade = float(input())
    if name not in dictionary.keys():
        dictionary[name] = list()
    dictionary[name].append(grade)

for (key,value) in dictionary.items():
    average_grade = sum(value)/len(value)
    dictionary[key] = average_grade

for (key,value) in dictionary.items():
    if value >= 4.5:
        print(f"{key} -> {value:.2f}")
"""   
for j in dictionary.keys():
    a = dictionary[name]
    b = len[name]
    average_grade = dictionary[name]/len[name]
    if average_grade < 4.5:
        del[name]
"""

