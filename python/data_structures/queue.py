from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Class creates an empty Queue when instantiated. Contains methods for modifying or analyzing the node contents of queue or stack.
    """


    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = self.rear


    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        current_front = self.front
        self.front = current_front.next
        return current_front.value


    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value


    def is_empty(self):
        return not self.front
