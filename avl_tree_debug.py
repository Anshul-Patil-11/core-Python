# implementation of AVL Trees

class node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 0

def getHeight(node):
    if node.left != None and node.right != None:
        node.height = 1 + max(node.left.height, node.right.height)
    elif node.left != None:
        node.height = node.left.height + 1
    elif node.right != None:
        node.height = node.right.height + 1
    else:
        node.height = 0
    return node.height

nodeC = node('C')
nodeB = node('B')
nodeE = node('E')
nodeA = node('A')
nodeD = node('D')
nodeG = node('G')
nodeF = node('F')
nodeH = node('H')

# root = nodeC
# root.left = nodeB
# root.right = nodeE
# nodeB.left = nodeA
# nodeE.left = nodeD
# nodeE.right = nodeG
# nodeG.left = nodeF 
# nodeG.right = nodeH

# inOrderTraversal(root)

def nodeAndHeightTraversal(node):
    if node == None:
        return 
    nodeAndHeightTraversal(node.left)
    nodeAndHeightTraversal(node.right)
    node.height = getHeight(node)
    print(node.value, node.height, end=", ")

# result = nodeAndHeightTraversal(root)

def getBalance(node):
    if node.left!=None and node.right!=None:
        node.right.height = getHeight(node.right)
        node.left.height = getHeight(node.left)
        return (node.right.height - node.left.height)
    elif node.left!= None:
        node.left.height = getHeight(node.left)
        return(0 - node.left.height - 1)
    elif node.right!=None:
        node.right.height = getHeight(node.right)
        return(node.right.height + 1)
    else:
        return 0

def rightRotate(x):
    oldX = x
    newX = oldX.left
    temp = newX.right
    oldX.left = temp
    newX.right = oldX
    oldX.height = getHeight(oldX) # Updating Heights of changed nodes
    newX.height = getHeight(newX)
    return newX

def leftRotate(y):
    oldY = y
    newY = y.right
    temp = newY.left
    oldY.right = temp
    newY.left = oldY
    oldY.height = getHeight(oldY) # Updating Heights of changed nodes
    newY.height = getHeight(newY)
    return newY

def insert(value, root):
    if root == None:
        return node(value)
    elif root.value == value:
        print("Node already Exists")
    elif value<root.value:
        root.left = insert(value, root.left)
    elif value>root.value:
        root.right = insert(value, root.right)

    # calc height and balance factor

    root.height = getHeight(root)
    print(f"height of node {root.value} is {root.height}")
    balanceFactorRoot = getBalance(root)
    print(f"The balance factor of node {root.value} is {balanceFactorRoot}")

    # rotate

    if balanceFactorRoot<-1:

        if getBalance(root.left)<0:
            # LL 
            print(f'performing right rotate on {root.value}\n')
            return rightRotate(root)
        elif getBalance(root.left)>0:
            # LR 
            root.left = leftRotate(root.left)
            print(f'performing left rotate on {root.left.value} then right rotate on {root.value}\n')
            return rightRotate(root)

    elif balanceFactorRoot>1:
        
        if getBalance(root.right)>0:
            # RR 
            print(f'performing left rotate on {root.value}\n')
            return leftRotate(root)
        elif getBalance(root.right)<0:
            # LR 
            root.right = rightRotate(root.right)
            print(f'performing right rotate on {root.right.value} then left rotate on {root.value}\n')
            return leftRotate(root)

    return root

def in_order_traversal(root):
    if root == None:
        return
    in_order_traversal(root.left)
    print(root.value, end=" ")
    in_order_traversal(root.right)

# Inserting Nodes
nodes = ['C','B','E','A','D','H','G','F']
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
nodes = ['M', 'D', 'T', 'B', 'H', 'P', 'W', 'F', 'J']


root = None

for letter in nodes:
    print(f'inserting {letter}')
    root = insert(letter, root)
    nodeAndHeightTraversal(root)
    print('\n')

in_order_traversal(root)

