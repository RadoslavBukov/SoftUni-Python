"""
Test Code	                                            Output

result = sequence_repeat('abc', 5)                      abcab
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)            I L
for item in result:
    print(item, end ='')
"""
class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= self.number:
            raise StopIteration

        value_to_return = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return value_to_return

# Test Code 2
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

# Test Code 2
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
