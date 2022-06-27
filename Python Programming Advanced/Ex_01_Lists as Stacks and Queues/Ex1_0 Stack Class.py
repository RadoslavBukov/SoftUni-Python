class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)

s = Stack()

for i in range(5, 10):  # s = [5, 6, 7, 8, 9]
    s.push(i)

print(s.pop())          # 9     s = [5, 6, 7, 8]
print(s.peek())         # 8     s = [5, 6, 7, 8]
print(s.count())        # 4     elements in stack