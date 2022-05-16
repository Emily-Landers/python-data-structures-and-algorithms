from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    # takes 2 linked lists and merge them so that the nodes alternate between the two lists and return a reference to the the zipped list
    current_a = a.head
    current_b = b.head

    while current_b and current_a:
        a.insert_after(current_a.value, current_b.value)
        current_a = current_a.next
        if current_a.next:
            current_a = current_a.next
        current_b = current_b.next

    if current_a == None or current_b == None:
        if current_b:
            return b
        if current_a:
            return a

    return a