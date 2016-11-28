class Node(object):
    def __init__(self, value):
        self.value = value
        self.adjlist = None

    def AddEdge(self, number):
        self.adjlist.append(number)

class Graph(object):
    def __init__(self):
        self.nodeList = []

    def AddNode(self, number):
        self.nodeList.append(Node(number))
        return self.nodeList[Node]
        print(self.nodeList)
        
    def AddEdge(self, number1, number2):
        for i in range (len(self.nodeList)):                
            number1.adjlist.append(number2.value)
            number2.adjlist.append(number1.value)

    def display(self):
        for i in range(len(nodeList)):
            print(nodeList(i).value)
            for j in range(len(nodeList[i].adjlst)):
                print(nodeList[i].adjlst[j])
                

if __name__ == '__main__':
    g = Graph()
    myNode1 = g.AddNode(4)
    myNode2 = g.AddNode(5)
    g.AddEdge(myNode1,myNode2)
    g.display()
    


