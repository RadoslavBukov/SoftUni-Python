"""
Test Code	                        Output
numbers = take_skip(2, 6)           0
for number in numbers:              2
    print(number)                   4
                                    6
                                    8
                                    10

numbers = take_skip(10, 5)          0
for number in numbers:              10
    print(number)                   20
                                    30
                                    40
"""
class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration

        return_value = self.iterations * self.step
        self.iterations += 1
        return return_value

# Input 1
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

# Input 2
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
