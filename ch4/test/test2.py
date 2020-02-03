

class Simple:
    stack: list

    def __init__(self, _stack):
        self.stack = _stack


s1 = Simple([1])
s2 = Simple([2])

# s1.stack = []
s1.stack.append(1)
s1.stack.append(2)
s1.stack.append(3)

print(s1.stack)

print(s2.stack)