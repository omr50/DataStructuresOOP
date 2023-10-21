class Stack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, item):
        self.items.append(item)
        if self.min:
            self.min.append(item if item < self.min[-1] else self.min[-1])
        else:
            self.min.append(item)

    def pop(self):
        if self.items:
            self.min.pop()
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def getMin(self):
        return self.min[-1] if self.min else None


stack = Stack()

stack.push(4)
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(1)
print(stack.items)

print(stack.min)


# use stack to determine balanced parenthesis


parenDict = {
    '{': '}',
    '[': ']',
    '(': ')'
}

string1 = '{[()]}'
string2 = '{}()[][]()'
string3 = '{}(())[}'

strings = [string1, string2, string3]
for string in strings:
    parenStack = Stack()
    for ch in string:
        if ch in parenDict:
            parenStack.push(ch)
        else:
            if parenStack.size() and ch == parenDict[parenStack.peek()]:
                parenStack.pop()
            else:
                break
    if parenStack.size():
        print("FALSE")
        break
    print("TRUE")
