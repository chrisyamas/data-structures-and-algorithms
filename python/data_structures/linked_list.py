
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


    def append(self, value):
        current = self.head
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        while current.next:
            current.next = new_node


    def insert_before(self, new_value, value):
        if not self.head:
            raise TargetError
        elif self.head.value == new_value:
            self.insert(value)
            return

        current = self.head

        while current:
            try:
                if current.next.value == new_value:
                    status_quo = current.next
                    current.next = Node(value, status_quo)
                    break
                current = current.next
            except:
                raise TargetError


    def insert_after(self, new_value, value):
        if not self.head:
            raise TargetError

        current = self.head

        while current:
            if current.value == new_value:
                current.next = Node(value, current.next)
                break
            if not current.next:
                raise TargetError
            current = current.next


class Node:
    def __init__(self, node_value=None, next_node=None):
        self.value = node_value
        self.next = next_node


class TargetError(Exception):
    """
    This is a custom exception.
    """
