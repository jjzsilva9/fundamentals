from BinaryTree import Node

class AVLTree:
    def __init__(self, *root):
        if root:
            self.root = root
        else:
            self.root = Node()

    