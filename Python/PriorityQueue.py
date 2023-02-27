import heapq
 
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
 
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print(self._queue)
        
 
    def pop(self):
        return heapq.heappop(self._queue)[-1]
        print(self._queue)

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
 
q = PriorityQueue()
 
q.push(Item('how'), 1)
q.push(Item('to'), 5)
q.push(Item('do'), 4)
q.push(Item('in'), 2)
q.push(Item('java'), 1)
 
q.pop()
Item('to')      #5
 
q.pop()
Item('do')      #4
 
q.pop()
Item('in')      #2
 
q.pop()
Item('how')     #1
 
q.pop()
Item('java')    #1


