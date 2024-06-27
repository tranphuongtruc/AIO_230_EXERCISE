class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_val = []

    def is_empty(self):
        return True if len(self.num_val) == 0 else False

    def is_full(self):
        return True if len(self.num_val) == self.capacity else False

    def pop(self):
        last_val = self.num_val.pop()
        return last_val

    def push(self, value):
        self.num_val.append(value)

    def top(self):
        return self.num_val[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
print()
