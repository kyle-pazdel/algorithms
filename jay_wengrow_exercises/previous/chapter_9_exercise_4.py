
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, char):
        return self.stack.append(char)

    def pop(self):
        return self.stack.pop(-1)

    def read(self):
        return self.stack[-1]


def reverse_string(string):
    stack = Stack()
    for c in string:
        stack.push(c)
    res = ""
    for c in range(0, len(string)):
        res += stack.pop()
    return res


print(reverse_string("abcde"))
