"""Treesort Algorithm that sorts the nodes in a tree in ascending order using the
in_order function and ."""
class BinTreeNode(object): #Node class
 
    def __init__(self, value): # Constructor
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item): #Inserts nodes into tree
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print ("Post Order",tree.value)
 
 
"""def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)"""
# My work
def in_order(tree): # Sorts the nodes in the tree
    currentNode = tree 
    stack = [] # empty stack (list)
    incomplete = True # Determines when the while loop has to stop
    while incomplete == True: # While loop for sorting the nodes in ascending order
        if currentNode != None: # appends the current node from the tree to the stack if current node is not none
            stack.append(currentNode)
            currentNode = currentNode.left
            #print(currentNode)
        else:
            if(len(stack)>0): # currentNode is assigned to the value of last node in the stack if length 
                currentNode = stack.pop() # of stack is greater than 0
                print("In Order",currentNode.value) #prints the sorted nodes in order
                currentNode = currentNode.right 
            else:
                incomplete = False # ends the while loop.

if __name__ == '__main__': # main
   
  t=tree_insert(None,6); # call to function to insert nodes into tree
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t) # function call to inorder
  print()
  postorder(t) # function call to postorder
