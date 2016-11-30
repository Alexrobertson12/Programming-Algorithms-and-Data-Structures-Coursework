"""Program that adds and delets nodes from a linked list."""
class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
 
class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    # My work        
    def delete(self,n):  # Function that deletes nodes from a linked list
        print("delete node", id(n) ) # Prints the id of the node that is to be deleted
        
        if n.prev != None: # if the previous node is not None, previous node is linked to next node
            n.prev.next = n.next
        else:               # else the head of the list skips n.
            self.head = n.next 
        if n.next != None: # if the next node is not None, the next node is linked to the previous node
            n.next.prev = n.prev
        else:     # else the tail of the node skips n.
            self.tail = n.prev
            
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))

        n=self.head
        while n!=None:
            print( "Node", id(n), end=", " )
            n=n.next
        print()
         
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    ourNode = Node(4)
    l.insert(l.head,ourNode)

    l.display()

    l.delete(ourNode)

    l.display()
