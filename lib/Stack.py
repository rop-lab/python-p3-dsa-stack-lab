class Stack:
    def __init__(self, items=None, limit=100):
        self.items = [] if items is None else items[:limit]
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) == self.limit

    def search(self, value):
        if value in self.items:
            return self.size() - self.items.index(value) - 1
        else:
            return -1
