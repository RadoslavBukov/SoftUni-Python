"""
Input           Output
100000          100001 100012 100023 100034 100045
100050

123456          123464 123475 123486 123497 123530 123541 123552 123563 123574 123585 123596 123640 123651 123662 123673 123684 123695 123750 123761 123772 123783 123794 123860 123871 123882 123893 123970 123981 123992
124000

299900          299970 299981 299992
300000

100115          No output
100120
"""
number_1 = int(input())
number_2 = int(input())

for number in range(number_1, number_2 + 1):
    number_to_str = str(number)
    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 ==0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)

    if sum_even == sum_odd:
        print(number, end=" ")