from data_structures.linked_list import LinkedList

class Hashtable():

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * self.size
        
    def set(self, key, value):
        index = self.hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            self._buckets[index] = LinkedList()
        
        self._buckets[index].insert((key, value))
        
    def hash(self, key):
        char_sum = 0
        if type(key) == str:
            for char in key:
                char_sum += ord(char)
        elif type(key) == int:
                char_sum = key
        char_sum *= 599
        index = char_sum % len(self._buckets)
        return index

    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
    
        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]

            current = current.next


    def contains(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]

        if bucket is None:
            return False
        
        current = bucket.head
        
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False
        

    def keys(self):
        keys = set()
        for bucket in self._buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    keys.add(container.value[0])
                    print(keys)
                    container = container.next
        return keys

