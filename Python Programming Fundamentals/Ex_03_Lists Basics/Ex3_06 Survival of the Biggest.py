"""
Input	                Output
10 9 8 7 6 5            10, 9, 8
3

1 10 2 9 3 8            10, 9, 3, 8
2
"""
text = str(input())
number = int(input())
text_list = text.split(" ")
int_list = []

for i in range (0, len(text_list)):
    int_list.append(int(text_list[i]))
for j in range (0, number):
    text_list.remove(min(text_list))

print(f'{", ".join([str(i) for i in text_list])}')

"""=========================
#Print 1:
for x in int_list:
    print(str(x)+", ",end="")
print("\b\b")                   (\b - trie edin simvol ot kraq na printa)
============================
#Print 2:
print(*int_list, sep=", ")      (sep = separator za delene)
"""