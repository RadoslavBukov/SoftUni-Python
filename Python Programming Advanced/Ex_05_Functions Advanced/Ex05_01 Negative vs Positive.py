"""
Input	                            Output
1 2 -3 -4 65 -98 12 57 -84	        -189
                                    137
                                    The negatives are stronger than the positives

1 2 3	                            0
                                    6
                                    The positives are stronger than the negatives
"""
def find_negative_positive_sums(*args):
    positive_sum = 0
    negative_sum = 0
    for number in args:
        if number >= 0:
            positive_sum += number
        else:
            negative_sum += number

    return positive_sum, negative_sum

numbers = [int(x) for x in input().split()]

positive_sum, negative_sum = find_negative_positive_sums(*numbers)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")