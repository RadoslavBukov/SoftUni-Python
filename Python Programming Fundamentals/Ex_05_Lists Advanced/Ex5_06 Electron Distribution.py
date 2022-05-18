"""
Input	        Output
10	            [2, 8]

44	            [2, 8, 18, 16]
"""
electrons_number = int(input())
shells=list()

for i in range(1, electrons_number+1):
    if electrons_number >= (2*(i**2)):
        shells.append(2*(i**2))
        electrons_number -= (2*(i**2))
    else:
        shells.append(electrons_number)
        break
print(shells)

#shells2 = [2*(i**2) if electrons_number >= (2*(i**2)) else shells.append(electrons_number) for i in range (1, electrons_number+1) ]
#print(shells2)