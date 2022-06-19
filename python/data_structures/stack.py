from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Class creates an empty Stack when instantiated. Contains methods for modifying or analyzing the node contents of a stack.
    """


    def __init__(self):
        self.top = None
        self.size = 0


    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1


    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        current_top = self.top
        self.top = self.top.next
        current_top.next = None
        self.size -= 1
        return current_top.value


    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


    def is_empty(self):
        return self.size == 0

