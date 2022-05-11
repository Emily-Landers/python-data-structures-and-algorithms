from data_structures.queue import Queue
from code_challenges.tree_breadth_first import breadth_first

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Traverse the tree in a pre-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: do something
            values.append(root.value)

            # Task 2: go left
            walk(root.left, values)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        Traverse the tree in an i-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: do something
            values.append(root.value)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        """
        Traverse the tree in a post-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: go right
            walk(root.right, values)

            # Task 3: do something
            values.append(root.value)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def find_maximum_value(self):

        if not self.root: return None

        def walk(root, max):

            if not root:
                return max

            if root.value > max:
                max = root.value

            max = walk(root.left, max)
            return walk(root.right, max)

        return walk(self.root, self.root.value)
    
    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)

    def breadth_first(self):
        return breadth_first(self)
    