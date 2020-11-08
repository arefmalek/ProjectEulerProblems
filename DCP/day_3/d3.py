class Node:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right

def Serialize(n):

    if (n.val != None and n.left != None):
        print(n.val, n.left.val)
        Serialize(n.left)
    elif(n.val != None and n.left == None):
        print(n.val)
        print("end left")

    if (n.val != None and n.right != None):
        print(n.val, n.right)
        Serialize(n.right)
    elif (n.val != None and n.right == None):
        print(n.val)
        print("end right")



# n = Node(3)
# n.left = Node(4, 5)
# n.right = Node(6, None, 8)
# print(n.right.val)

node = Node('root', Node('left', Node('left.left')), Node('right'))

Serialize(node)