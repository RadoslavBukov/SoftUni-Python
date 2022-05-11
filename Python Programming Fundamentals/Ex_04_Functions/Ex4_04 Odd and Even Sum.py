"""
Input	                Output
1000435	                Odd sum = 9, Even sum = 4

3495892137259234	    Odd sum = 54, Even sum = 22
"""
def sum_numbers(a):
    sum_even = 0
    sum_odd = 0
    for digit in str(a):
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")

x = str(input())
sum_numbers(x)