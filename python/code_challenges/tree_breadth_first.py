from data_structures.queue import Queue


def breadth_first(tree):
    tree_queue = Queue()
    values = []
    if not tree.root:
        return values
    if not tree_queue.front:
        tree_queue.enqueue(tree.root)
    while tree_queue.front:
        root_node = tree_queue.dequeue()
        values.append(root_node.value)
        if root_node.left:
            tree_queue.enqueue(root_node.left)
        if root_node.right:
            tree_queue.enqueue(root_node.right)

    return values
