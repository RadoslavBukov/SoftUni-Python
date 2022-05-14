"""
Input	    Output 	                            Comments
6	        We have a perfect number!	        1 + 2 + 3

28	        We have a perfect number!	        1 + 2 + 4 + 7 + 14

1236498	    It's not so perfect.
"""
def perfect(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    if sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

x = int(input())
perfect(x)
