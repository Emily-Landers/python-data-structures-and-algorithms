from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                transfer = self.stack1.pop()
                self.stack2.push(transfer)
        return self.stack2.pop()
