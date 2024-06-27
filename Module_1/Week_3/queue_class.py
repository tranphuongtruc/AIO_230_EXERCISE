class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_val = []

    def is_empty(self):
        return True if len(self.num_val) == 0 else False

    def is_full(self):
        return True if len(self.num_val) == self.capacity else False

    def dequeue(self):
        first_val = self.num_val.pop(0)
        return first_val

    def enqueue(self, value):
        self.num_val.append(value)

    def front(self):
        return self.num_val[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
