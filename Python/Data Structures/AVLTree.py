from BinaryTree import Node

class AVLTree:
    def __init__(self, *root):
        if root:
            self.root = Node(root[0])
        else:
            self.root = None

    def insert(self, node):
        self.root.insert(node)

    #def rebalance(self, node):

    def rotateLeft(self, node):
        if node.right:
            if node.right.left:
                temp = node.right.left
                node.right.left = node
                node.right = temp
            else:
                node.right.left = node
                node.right = None
        return node.right

    def rotateRight(self, node):
        if node.left:
            if node.left.right:
                temp = node.left.right
                node.left.right = node
                node.left = temp
            else:
                node.left.right = node
                node.left = None
        return node.left

    def height(self, node):
        if not node:
            return 0
        if not (node.left or node.right):
            return 1
        left = node.left or None
        right = node.right or None
        return 1 + max(self.height(left), self.height(right))
    
a = AVLTree(7)
a.insert(5)
a.insert(11)
a.insert(9)
a.insert(18)
a.insert(15)
a.insert(21)
a.root.nlr()
print("Height: " + str(a.height(a.root)))
print("-------")
a.root = a.rotateLeft(a.root)
a.root.nlr()
print("Height: " + str(a.height(a.root)))