"""
Input	                    Output
3                           cute - adorable, charming
cute                        smart - clever
adorable
cute
charming
smart
clever

2                           task – problem, assignment
task
problem
task
assignment
"""
count = int(input())
dictionary = dict()

for i in range(count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = list()

    dictionary[word].append(synonym)