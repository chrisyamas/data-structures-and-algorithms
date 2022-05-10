class BinaryTree:
    """
    Contains methods for each of the three types of depth first Binary Tree traversals.
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def traverse(root, values):
            if not root:
                return

            values.append(root.value)
            traverse(root.left, values)
            traverse(root.right, values)

        pre_ordered_vals = []
        traverse(self.root, pre_ordered_vals)
        return pre_ordered_vals

    def in_order(self):
        def traverse(root, values):
            if not root:
                return
            traverse(root.left, values)
            values.append(root.value)
            traverse(root.right, values)

        in_ordered_vals = []
        traverse(self.root, in_ordered_vals)
        return in_ordered_vals

    def post_order(self):
        def traverse(root, values):
            if not root:
                return
            traverse(root.left, values)
            traverse(root.right, values)
            values.append(root.value)

        post_ordered_vals = []
        traverse(self.root, post_ordered_vals)
        return post_ordered_vals

    def find_max(self):
        vals = self.post_order()
        max_value = vals[0]
        for value in vals:
            if value > max_value:
                max_value = value
        return max_value

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
