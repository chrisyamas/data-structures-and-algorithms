
class LinkedList:
    """
    This module allows creation of a singly linked list by making nodes with set values and adding them to the beginning of the list.
    """

    def __init__(self):
        self.head = None
        self.list = []

    def __str__(self):
        str = ''
        current = self.head
        if self.head == None:
            return 'NULL'
        while current:
            str += f"{{ {current.value} }} -> "
            current = current.next
        str += 'NULL'
        return str.replace("'","")

    def insert(self, value=None):
        self.head = Node(value, self.head)

    def includes(self, query):
        current = self.head
        while current:
            if current.value == query:
                return True
            current = current.next
        return False


class Node:
    def __init__(self, node_value=None, next_node=None):
        self.value = node_value
        self.next = next_node


class TargetError:
    pass
