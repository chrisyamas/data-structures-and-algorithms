
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

    def insert_before(self, value, new_value):
        if self.head == None:
            raise TargetError
        elif self.head.value == new_value:
            self.insert(new_value)
            return
        current = self.head
        while current:
            try:
                if current.next.value == value:
                    status_quo = current.next
                    current.next = Node(new_value, status_quo)
                    break
                current = current.next
            except:
                raise TargetError

    def insert_after(self, value, new_value):
        if self.head == None:
            raise TargetError
        current = self.head
        while current:
            if current.value == 

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
