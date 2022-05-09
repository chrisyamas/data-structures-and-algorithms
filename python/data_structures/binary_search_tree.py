from re import T
from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Contains methods for both adding a new node to a BST and searching a BST to see if a particular value is contained by any of its nodes.
    """

    def add(self, value):
        def traverse(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                if root.left:
                    traverse(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    traverse(root.right, new_node)
                else:
                    root.right = new_node

        input_node = Node(value)
        if not self.root:
            self.root = input_node
            return
        traverse(self.root, input_node)

    def contains(self, value):
        if not self.root:
            return False
        def traverse(root, value):
            if root.value == value:
                return True
            elif root.value > value:
                if root.left:
                    return traverse(root.left, value)
            elif root.value < value:
                if root.right:
                    return traverse(root.right, value)
            return False

        return traverse(self.root, value)
