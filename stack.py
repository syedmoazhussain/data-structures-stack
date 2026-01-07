class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Removed:", stack.pop())
