from PriorityQueue import Queue
class WeightedGraph:
    def __init__(self, nodes, weights):
        self.adj_matrix = []
        self.adj_list = {}
        for node1 in nodes:
          for node2 in nodes

        for node in self.nodes:
            self.adj_list[node]=[]

    def printList(self):
        for node in self.nodes:
            print(node, "-->", self.adj_list[node])

    def addNode(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def deleteNode(self, u):
        for node in self.adj_list:
            if node[0] or node[1] == u:
                self.adj_list[node].pop()
                
          