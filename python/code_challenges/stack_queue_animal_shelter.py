from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_obj = Queue()
        self.cat_obj = Queue()

    def enqueue(self, animal):
        pass

    def dequeue(self, pref):
        pass

class Dog:
    def __init__(self):
        self.type = 'dog'


class Cat:
    def __init__(self):
        self.type = 'cat'
