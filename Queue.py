class Queue:
    def __init__(self):
        self.last = 0
        self.first = 0
        self.q = []

    def enQueue(self, val):
        self.q.append(val)
        self.last+=1

    def deQueue(self):
        self.first += 1
        
    def isEmpty(self):
        if self.last == self.first:
            return True

    def isFull(self):
        if self.first == 0:
            return True

    def look(self):
        return self.q[self.first:self.last]

