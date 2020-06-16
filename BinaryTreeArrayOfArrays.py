#Rachel Herman

nodes = [[None, 10, None],
         [None,  4, None],
         [None,  6, None],
         [None,  2, None],
         [None,  3, None],
         [None,  1, None],
         [None, 17, None],
         [None, 12, None],
         [None, 15, None],
         [None, 20, None],
         [None,  8, None]]
''' #also works with this ex group of nodes
nodes = [[None, 16, None],
         [None,  7, None],
         [None,  8, None],
         [None, 21, None],
         [None,  5, None],
         [None,  9, None],
         [None,  9, None],
         [None,  2, None],
         [None,  1, None],
         [None,  3, None],
         [None,  4, None]]
'''
llink = 0
data = 1
rlink = 2
root = None

myStack = []
myStackFilledElements = 0

traversal = []

def main():

    for i in range(11):
        insertNode(nodes[i], i)
    
    traverseAndPrint(root)
    print(traversal)


def insertNode(node, i):
    global root
    global nodes

    #for node in Nodes:
    if (root == None):
        root = node

        
    else:#not the root
        tempRoot = root
        flag = True
        while flag:                
            if (tempRoot[data] >= nodes[i][data]): #root is greater than or equal (this node is less)
                if (tempRoot[llink] == None):
                    tempRoot[llink] = i #setting this nodes link
                    flag = False
                    
                else: #there is already a llink
                    tempRoot = nodes[tempRoot[llink]]

               
            else: #root is less than current node
                if (tempRoot[rlink] == None):
                    tempRoot[rlink] = i
                    flag = False

                else:
                    tempRoot = nodes[tempRoot[rlink]]
                    
def traverseAndPrint(root):
    global myStack
    
    currentNode = root

    linkNotNone = True
    while True:
        while linkNotNone:
            myStackPush(currentNode)
            nextNodeIndex = currentNode[llink]
            if (nextNodeIndex == None):
                linkNotNone = False
            else:
                currentNode = nodes[nextNodeIndex]

        if (isMyStackEmpty()):
            break
            
        currentNode =  myStackPop()
        traversal.append(currentNode[data])
        nextNodeIndex = currentNode[rlink]
        if (nextNodeIndex == None):
            linkNotNone = False
        else:
            currentNode = nodes[nextNodeIndex]
            linkNotNone = True
              

def myStackPush(node):
    global myStack
    global myStackFilledElements
    myStack.append(node)
    myStackFilledElements += 1
        
def myStackPop():
    global myStackFilledElements
    myStackFilledElements-=1
    return myStack.pop()

def isMyStackEmpty():
    if myStackFilledElements == 0:
        return True #yes, it is empty
    else:
        return False #myStack is not empty

main()
        
    
    

