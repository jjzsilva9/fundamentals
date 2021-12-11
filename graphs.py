from queue import Queue
import queue
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}

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

    def breadthfirstsearch(self, start, target):
        self.visited = {} #Makes a dictionary to track nodes that have been visited
        self.queue = Queue() #Makes a queue
        self.current = start #Sets start node to the current
        self.found = False #Bool value for when to stop searching
        for node in self.adj_list:
            self.visited[node] = False #Sets dictionary to false
        print(self.visited)
        while not self.found:
            done = True #Next 4 lines check if all nodes have been visited or not
            for node in self.visited:
                if node is False:
                    done = False
            if done and self.current != target:
                print(f"{target} is not in the graph!")
                return False
            self.visited[self.current] = True #Sets current node visited value to true
            if self.current == target: #Check for target value
                self.found = True
                print(f"Found {self.current}!")
                return self.current
            else:
                print(f"Not found - currently at {self.current}")
                print(self.visited)
                for node in self.adj_list[self.current]: #Adds next nodes to queue
                    print(node)
                    if not self.visited[node]:
                        self.queue.put(node)
            self.current = self.queue.get() #Increments to next queue value

    def depthfirstsearch(self, start, target, visitedList):
        if len(visitedList) != 0:
            self.visited = visitedList
        else:
            self.visited = {}
            for node in self.adj_list:
                self.visited[node] = False
        self.current = start
        self.visited[self.current] = True
        print(self.visited)
        if self.current == target:
            print(f"Found {target}!")
            return self.current
        else:
            for node in self.adj_list[self.current]:       
                if not self.visited[node]:
                    self.depthfirstsearch(node, target, self.visited)
                
            
            


        

nodes=["A", "B", "C", "D", "E"]
graph = Graph(nodes)

E = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("C", "E")]

for v in E:
    graph.addNode(v[0], v[1])

graph.printList()

graph.breadthfirstsearch("A", "H")

graph.depthfirstsearch("A", "E", {})