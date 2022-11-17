"""
Test Code	                    Output

take = solution()[0]            [0.5, 1.0, 1.5, 2.0, 2.5]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]            []
halves = solution()[1]
print(take(0, halves()))
"""
def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)

# Test Code 1
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# Test Code 2
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

