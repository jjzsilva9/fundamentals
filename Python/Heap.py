class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __init__(self, *root):
        if not root:
            self.heap = []
            self.size = 0
        else:
            self.heap = [root]
            self.size = 1

    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        index = len(self.heap) - 1
        parent = (index - 1) // 2 if index != 0 else 0
        print(node, self.heap[parent])
        while node < self.heap[parent]:
            self.heap[index] = self.heap[parent]
            self.heap[parent] = node
            index = parent
            parent = (index - 1 // 2) if index != 0 else 0

    def insertArray(self, nodes):
        for node in nodes:
            self.insert(node)
        

    def extractMin(self):
        m = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        index = 0
        while True:
            try:
                if self.heap[index] > self.heap[2*index+1]:
                    self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
                    index = 2*index+1
                elif self.heap[index] > self.heap[2*(index+1)]:
                    self.heap[index], self.heap[2*(index+1)] = self.heap[2*(index+1)], self.heap[index]
                    index = 2*(index+1)
                else:
                    break
            except:
                break
        return m


h = MinHeap()
h.insertArray([2, 4, 9, 18, 5, 11, 10, 21, 31, 8, 7])
print(h.heap)
h.extractMin()
print(h.heap)
        