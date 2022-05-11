from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Class creates an empty Stack when instantiated. Contains methods for modifying or analyzing the node contents of a stack.
    """


    def __init__(self):
        self.top = None


    def push(self, value):
        self.top = Node(value, self.top)


    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        current_top = self.top
        self.top = self.top.next
        current_top.next = None
        return current_top.value


    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


    def is_empty(self):
        return not self.top

