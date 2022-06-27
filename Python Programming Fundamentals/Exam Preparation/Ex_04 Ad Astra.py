"""
Input
#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

Output
You have food to last you for: 2 days!
Item: Bread, Best before: 19/03/21, Nutrition: 4000
Item: Apples, Best before: 08/10/20, Nutrition: 200
Item: Carrots, Best before: 06/08/20, Nutrition: 500

Input
$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|

Output
You have food to last you for: 9 days!
Item: Fish, Best before: 24/12/20, Nutrition: 8500
Item: Ice Cream, Best before: 03/10/21, Nutrition: 9000
Item: Milk, Best before: 05/09/20, Nutrition: 2000

Input                                                       Output
Hello|#Invalid food#19/03/20#450|$5*(@                      You have food to last you for: 0 days!
"""
import re
import math
text = input()
calories = 0

#regex = r"(?<=([|#]))[A-Za-z ]+\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1[0-9]+(?=\1)"
regex = r"(?<=([|#]))([A-Za-z]+ ?[A-Za-z]*)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1[0-9]+(?=\1)"
matches = re.finditer(regex, text)
item_number = 0

output = {}
item_list = list()
for match in matches:
    item_list.append(match.group())

for item in item_list:
    if "#" in item:
        item = item.split("#")
    else:
        item = item.split("|")
    if int(item[2]) < 10000:
        output[item_number] = dict()
        output[item_number]['Name'] = item[0]
        output[item_number]['Date'] = item[1]
        output[item_number]['Calories'] = item[2]
        calories += int(output[item_number]["Calories"])
        item_number += 1

print(f"You have food to last you for: {math.floor(calories/2000)} days!")

for key in output.keys():
    print(f"Item: {output[key]['Name']}, Best before: {output[key]['Date']}, Nutrition: {output[key]['Calories']}")

"""
output = {}
item_list = list()
for match in matches:
    item_list.append(match.group())

for item in item_list:
    if "#" in item:
        item = item.split("#")
    else:
        item = item.split("|")
    if int(item[2]) < 10000:
        if item[0] not in output.keys():
            output[item[0]] = dict()
        output[item[0]]['Date'] = item[1]
        output[item[0]]['Calories'] = item[2]
        calories += int(output[item[0]]["Calories"])

print(f"You have food to last you for: {math.floor(calories/2000)} days!")

for key in output.keys():
    print(f"Item: {key}, Best before: {output[key]['Date']}, Nutrition: {output[key]['Calories']}")
"""