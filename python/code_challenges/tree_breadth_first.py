from data_structures.queue import Queue

def breadth_first(tree):
    if not tree or tree.root is None:
        return []
    else:
        q = Queue()
        list = []

        q.enqueue(tree.root)

        while not q.is_empty():
            front = q.dequeue()
            list.append(front.value)
            if front.left:
                q.enqueue(front.left)
            if front.right:
                q.enqueue(front.right)
        print(f"list: {list}")
        return list
