class Node:

    def __init__(self, data):
        self.data = data
        self.pointer = []
        self.links = []

    def addPointer(self, Node):
        self.pointer.append(Node)
        Node.links.append(self)

Home = Node(1)
Info = Node(1)
Gallery = Node(1)
Camera = Node(1)
Prices = Node(1)

Home.addPointer(Gallery)
Gallery.addPointer(Home)
Gallery.addPointer(Camera)
Gallery.addPointer(Prices)
Camera.addPointer(Home)
Camera.addPointer(Prices)
Prices.addPointer(Camera)

nodes = [Home, Info, Gallery, Camera, Prices]

for i in range(5):
    for node in nodes:
        pagesRank = 0.15
        for link in node.links:
            pagesRank += 0.85 * (link.data/len(link.pointer))
        node.data = pagesRank

for node in nodes:
    print(node.data)

