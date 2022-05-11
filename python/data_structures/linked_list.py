class Node:
 
    
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
        
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None
        
    def __str__(self):
        # returns a collection of all values within linked list
        string = ""
        current = self.head
        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        return string + "NULL"
        
    def insert(self, value):
        #creating a new node with the correct value
       self.head = Node(value, self.head)
       
    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
             return True
            current = current.next
        else:
            return False  
    
    def insert_before(self, target, value):
        # adds a new node with the given value before target node
        current = self.head
        try:
            if current.value == target:
                self.insert(value)
            else:
                while current.value:
                    if current.next.value == target:
                        after = current.next
                        current.next = Node(value, after)
                        return Node(value, after)
                current = current.next
        except:
            raise TargetError
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        
    def insert_after(self, target, value):
        # adds a new node with the given value after target node
        current = self.head
        try:
            while current.value:

                if current.value == target:
                    after = current.next
                    current.next = Node(value, after)
                    return Node(value, after)
                current = current.next
        except:
            raise TargetError

    def kth_from_end(self, target):
        # Returns the node’s value that is k places from the tail of the linked list.
        current = self.head
        length = 0

        counter = self.head
        while counter.next:
            length += 1
            counter = counter.next

        if length < target:
            raise TargetError
        try:
            for i in range(length-target):
                current = current.next
            return current.value
        
        except:
            raise TargetError
        

 
class TargetError(Exception):
    pass
