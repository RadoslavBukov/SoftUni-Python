"""
Input	    Output              Input       Output
23          19                  1           -12
6                               17
10                              30
"""
def sum_numbers(a,b):
    return a+b

def subtract(d,c):
    return d - c

num1, num2, num3 = int(input()), int(input()), int(input())

print(subtract(sum_numbers(num1,num2),num3))