class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __init__(self, root):
        self.heap = [root]
        self.size = 1

    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        index = len(heap) - 1
        parent = index - 1 // 2
        while node < self.heap[parent]:
            self.heap[parent] = self.heap[index], self.heap[index] = self.heap[parent]
            index = parent
            parent = index - 1 // 2

    def extractMin(self):
        m = self.heap[0]
        