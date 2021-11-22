class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def lrn(self):
        if self.left:
            self.left.lrn()
        if self.right:
            self.right.lrn()
        print(self.data)

    def nlr(self):
        print(self.data)
        if self.left:
            self.left.lrn()
        if self.right:
            self.right.lrn()
        

    def lnr(self):
        if self.left:
            self.left.lrn()
        print(self.data)
        if self.right:
            self.right.lrn()
        




root = Node(1)
root.insert(2)
root.insert(3)
root.insert(0)
root.insert(4)
root.insert(7)
root.insert(5)
root.insert(6)
root.lrn()
root.nlr()
root.lnr()



