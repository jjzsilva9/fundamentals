from PriorityQueue import Queue
class WeightedGraph:
    def __init__(self, nodes):
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node]=[]

    def printList(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])

    def addLink(self, u, v, weight):
        self.adj_list[u].append({v: weight})
        self.adj_list[v].append({u: weight})

    def addNode(self, node):
        self.adj_list[node] = []

    def deleteNode(self, u):
        for node in self.adj_list:
            if node[0] or node[1] == u:
                self.adj_list[node].pop()
                
          