"""
Test Code	                                                    Output
result = dictionary_iter({1: "1", 2: "2"})                      (1, '1')
for x in result:                                                (2, '2')
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})          ("name", "Peter")
for x in result:                                                ("age", 24)
    print(x)
"""
class dictionary_iter:

    def __init__(self, data):
        self.items = list(data.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items):
            raise StopIteration
        return_value = self.items[self.idx]
        self.idx += 1
        return return_value


# Test Code 1
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Test Code 2
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
