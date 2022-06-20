from attr import has
from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Module implements a hash table.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = self.size * [None]

    def __eq__(self, other):
        for key in self.keys():
            if self.get(key) != other.get(key):
                return False
        return True

    def set(self, key, value):
        index = self.hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            self._buckets[index] = LinkedList()
        self._buckets[index].insert((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            return False
        current = bucket.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        keys = set()
        for bucket in self._buckets:
            if bucket:
                current = bucket.head
                while current:
                    keys.add(current.value[0])
                    current = current.next
        return keys

    def hash(self, key):
        if type(key) is str:
            ascii_ = [ord(char) for char in key]
            hashed = sum(ascii_)
        if type(key) is int:
            hashed = key
        hash_index = (hashed * 599) % self.size
        return hash_index
