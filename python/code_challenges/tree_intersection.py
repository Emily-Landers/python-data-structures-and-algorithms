from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    first = BinaryTree.pre_order(tree1)
    second = BinaryTree.pre_order(tree2)
    x = set(first)
    y = set(second)
    return x.intersection(y)
