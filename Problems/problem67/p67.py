class Node:
    """Connecting all the values in a tree like thing"""

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.lsum = 0
        self.rsum = 0

with open("nums.txt") as f:
    pog = []

    for line in f:
        line = line.rstrip()
        nums = [int(info) for info in line.split(" ")]
        pog.append(nums)

for layer, arr in enumerate(pog):
    if layer == 0: continue

    for ind, value in enumerate(arr):
        left = 0
        right = 0
        if (ind - 1 >= 0): left = pog[layer - 1][ind - 1]
        if (ind < layer): right = pog[layer - 1][ind]

        arr[ind] += max(left, right)

print(max(pog[-1]))
