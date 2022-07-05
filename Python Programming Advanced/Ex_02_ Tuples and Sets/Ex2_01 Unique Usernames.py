"""
Input	        Output                          Input           Output
6                                               10              Peter
George          George                          Peter           Maria
George          Peter                           Maria           George
George          NiceGuy1234                     Peter           Steve
Peter                                           George          Alex
George                                          Steve
NiceGuy1234	                                    Maria
                                                Alex
                                                Peter
                                                Steve
                                                George
"""
n = int(input())
name_set = set()

for _ in range(n):
    name = input()
    name_set.add(name)

print('\n'.join(name_set))