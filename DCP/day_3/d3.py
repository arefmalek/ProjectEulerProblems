class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def Serialize(n):

    print(n.val, n.left, n.right)

    if (n.val != None and n.left != None):
        Serialize(n.left)
    elif(n.val != None and n.left == None):
        print("end left")

    if (n.val != None and n.right != None):
        Serialize(n.right)
    elif (n.val != None and n.right == None):
        print("end right")
        
    print(n.val, n.left, n.right)



node = Node('root',
 Node('left', Node('left.left')),
 Node('right'))

#print(node.val, node.left, node.right)
Serialize(node)