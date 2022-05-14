from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)
        elif animal.type == 'Cat':
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dogs.dequeue()
        elif pref == 'cat':
            return self.cats.dequeue()
        else:
            return None


class Dog:
    def __init__(self):
        self.type = 'Dog'


class Cat:
    def __init__(self):
        self.type = 'Cat'
