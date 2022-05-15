from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(tree):

    def fizz_buzz(value):
        value = int(value)
        if value % 15 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    fizz_queue = Queue()
    new_kary = []
    fizz_tree = KaryTree(tree.root)
    fizz_queue.enqueue(fizz_tree.root)
    while not fizz_queue.is_empty():
        node = fizz_queue.dequeue()
        new_node = fizz_buzz(node.value)
        new_kary.append(new_node)
        for kid in node.children:
            fizz_queue.enqueue(kid)

    return new_kary

