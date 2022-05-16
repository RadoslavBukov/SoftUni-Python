"""
Input	                                            Output
arp, live, strong                                   ['arp', 'live', 'strong']
lively, alive, harp, sharp, armstrong

tarp, mice, bull                                    []
lively, alive, harp, sharp, armstrong
"""
input_list_1 = input().split(", ")
input_list_2 = input().split(", ")

substring = list()
substring = [x for x in input_list_1 for y in input_list_2 if x in y]

res = []
[res.append(x) for x in substring if x not in res]

print(res)

""" #Variant1 working
substring = list()

for i in range(len(input_list_1)):
    for n in range(len(input_list_2)):
        if input_list_1[i] in input_list_2[n]:
            substring.append(input_list_1[i])

res = []
[res.append(x) for x in substring if x not in res]

print(res)
"""

""" #Variant2
substring = input().split(', ')
sentence = input()
result = [el for el in substring if el in sentence]
print(result)
#It takes second input(sentence) as sentence and check if the words/string from first input substring is in the sentence.
"""