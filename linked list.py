class Node:
    def __init__(self, datapointer=None):
        self.datapointer = datapointer
        self.nextpointer = None

class LinkedList:
    def __init__(self):
        self.headpointer = None

    def listprint(self):
        printpointer = self.headpointer
        while printpointer is not None:
            print (printpointer.datapointer)
            printpointer = printpointer.nextpointer

    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next pointer to existing node
        NewNode.nextpointer = self.headpointer
        self.headpointer = NewNode

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headpointer is None:
            self.headpointer = NewNode
            return
        laste = self.headpointer
        while(laste.nextpointer):
            laste = laste.nextpointer
        laste.nextpointer=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextpointer = middle_node.nextpointer
        middle_node.nextpointer = NewNode

    # Function to remove node
    def RemoveNode(self, Removekey):

        Headpointer = self.headpointer

        if (Headpointer is not None):
            if (Headpointer.datapointer == Removekey):
                self.headpointer = Headpointer.nextpointer
                Headpointer = None
                return

        while (Headpointer is not None):
            if Headpointer.datapointer == Removekey:
                break
            prev = Headpointer
            Headpointer = Headpointer.nextpointer

        if (Headpointer == None):
            return

        prev.nextpointer = Headpointer.nextpointer

        Headpointer = None

list = LinkedList()
list.AtBeginning("Mon")
list.AtBeginning("Tue")
list.AtBeginning("Wed")
list.AtBeginning("Thu")
list.RemoveNode("Tue")
list.listprint()

