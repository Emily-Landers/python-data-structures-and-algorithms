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
    
    def insert_before(self, new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            #self.head = new_node 
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

class TargetError:
    pass
