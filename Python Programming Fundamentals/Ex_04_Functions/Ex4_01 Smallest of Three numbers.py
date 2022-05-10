"""
Input	    Output          Input       Output
2           2               600         123
5                           342
3	                        123
"""
def smallest(a,b,c):
    return min(a,b,c)

num1, num2, num3 = int(input()), int(input()), int(input())

print(smallest(num1,num2,num3))