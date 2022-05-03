from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, value):
        while len(self.stack1) != 0:
            self.stack1.pop()
            self.stack1.append(value)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
            
    def dequeue(self):
        if len(self.stack1) == 0:
            print("is empty")
        value = self.stack1[-1]
        self.stack1.pop()
        return value
q = PseudoQueue()
print(q.stack1)        
