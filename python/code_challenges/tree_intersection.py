from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    tree_a_values_hash = Hashtable()
    common_hash = Hashtable()
    tree_a_values_list = tree_a.pre_order()
    for element in tree_a_values_list:
        tree_a_values_hash.set(element, True)
    tree_b_values_list = tree_b.pre_order()
    for element in tree_b_values_list:
        if tree_a_values_hash.contains(element):
            common_hash.set(element, True)
    common_values = common_hash.keys()
    return common_values
