"""
Test Code	                                    Output
iterator = countdown_iterator(10)               10 9 8 7 6 5 4 3 2 1 0
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)                0
for item in iterator:
    print(item, end=" ")
"""
class countdown_iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        value_to_return = self.count
        self.count -= 1
        return value_to_return

# Test Code 1
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Test Code 2
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
