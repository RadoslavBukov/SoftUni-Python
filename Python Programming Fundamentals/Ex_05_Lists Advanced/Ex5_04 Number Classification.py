"""
Input	                                            Output
1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33	        Positive: 1, 0, 5, 3, 4, 12, 19
                                                    Negative: -2, -100, -20, -33
                                                    Even: -2, 0, 4, -100, -20, 12
                                                    Odd: 1, 5, 3, 19, -33

1, 2, 53, 2, 21	                                    Positive: 1, 2, 53, 2, 21
                                                    Negative:
                                                    Even: 2, 2
                                                    Odd: 1, 53, 21
"""

input_version = input().split(", ")

positive = [x for x in input_version if int(x) >= 0]
negative = [x for x in input_version if int(x) < 0]
even = [x for x in input_version if int(x) % 2 == 0]
odd = [x for x in input_version if int(x) % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")