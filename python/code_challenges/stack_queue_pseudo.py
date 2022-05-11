from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()


    def enqueue(self, value):
        self.inbox.push(value)


    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                move_over = self.inbox.pop()
                self.outbox.push(move_over)
        return self.outbox.pop()
