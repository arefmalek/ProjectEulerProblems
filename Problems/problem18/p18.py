class Node:
    """Connecting all the values in a tree like thing"""

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.lsum = 0
        self.rsum = 0

with open("problem18/nums.txt") as f:
    

    for line in f:
        line = line.rstrip()
        pog.append(line.split(" "))

print(pog)