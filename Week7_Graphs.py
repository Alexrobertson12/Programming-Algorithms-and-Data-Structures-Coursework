"""Unweighted Graph data structure implementation"""
import collections

class Graph: # Creates graph datatype
    def __init__(self): # class constructor, creates graph as dictionary
        self.unweighteddict = {}

    def insertNode(self, node): # inserts a node into the graph
        if node not in self.unweighteddict:
            self.unweighteddict[node] = []
        else:
            print("Node already here")

    def insertEdge(self, nodeA, nodeB): # inserts an edge that links two nodes in the graph
        if nodeA in self.unweighteddict and nodeB in self.unweighteddict:
            if nodeB not in self.unweighteddict[nodeA]: #nodeB is appended to nodeA if nodeB is not in unweighteddictionary.
                self.unweighteddict[nodeA].append(nodeB)
            if nodeA not in self.unweighteddict[nodeB]: #nodeA is appended to nodeB if nodeB is not in unweighteddictionary
                self.unweighteddict[nodeB].append(nodeA)
        else:
            print("Node not found")


# create the unweighted graph by inserting edges and nodes
graph = Graph()
graph.insertNode(1)
graph.insertNode(2)
graph.insertNode(3)
graph.insertNode(4)
graph.insertNode(5)
graph.insertNode(6)
graph.insertNode(7)
graph.insertNode(8)

graph.insertEdge(1,2)

graph.insertEdge(1,3)

graph.insertEdge(3,4)

graph.insertEdge(4,5)

graph.insertEdge(5,6)

graph.insertEdge(6,7)

graph.insertEdge(7,8)

graph.insertEdge(8,1)

print(graph.unweighteddict)

"""PSEUDOCODE
CLASS Graph:
    __INIT__(self)
       self.unweighteddct <- {}

    INSERT-NODE(self, node)
       IF node IS NOT IN self.unweighteddct:
           self.unweighteddict[node] <- []
       ELSE
           print("Node already here")

    INSERT-EDGE(self, nodeA, nodeB)
       IF nodeA in self.unweighteddict[nodeA] AND nodeB IN self.unweighteddict
           IF nodeB IS NOT IN self.unweighteddict[nodeA]
              append nodeB to self.unweighted[nodeA]
           IF nodeA IS NOT IN self.unweighteddict[nodeB]
              append nodeA to self.unweighted[nodeB]
           ELSE:
              print("Node not found")

graph = Graph()
graph.insertNode(Node)

graph.insertEdge(Node1,Node2)
"""
    
##Traversals
"""Depth first search"""
def Depth_First_Search(graph, v):
    S = [] # empty stack
    visited = [] 
    S.append(v) #append search value to stack
    while S != []: # #while loop creates list of visited nodes while Stack is not empty
        u = S.pop()
        if u not in visited: 
            visited.append(u)
            for i in graph.unweighteddict: #append e to Stack for all edges from in graph.
                for e in graph.unweighteddict[i]:
                    S.append(e)
    return visited

#BFS
"""Bredth First Search"""
def Breadth_First_Search(graph, v, lendfs):
    class Queue: # creates queue class
        def __init__(self):
            self.contents = []
        def empty(self):
            return self.contents == []
        def enqueue(self, content):
            self.contents.insert(0,content)
        def dequeue(self):
            return self.contents.pop()
        def length(self):
            return len(self.items)    
    Q = Queue() # assigns Q to queue class
    visited = []
    Q.enqueue(v)
    while Q != []: #while loop creates list of visited nodes while Queue is not empty
        u = Q.dequeue()
        if u not in visited:
            visited.append(u)
        for i in graph.unweighteddict: #enqueue e to Queue for all edges in graph.
            for e in graph.unweighteddict[i]:
                Q.enqueue(e)
        if len(visited) == len(dfs):
            return visited
            break
        

v = 1 #search value
print()
dfs = Depth_First_Search(graph, v)
print("Depth First Search", dfs)
print()
lendfs = len(dfs)
print("Breadth First Search", Breadth_First_Search(graph, v, lendfs))
