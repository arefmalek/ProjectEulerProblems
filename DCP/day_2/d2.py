import numpy as np
import math

def v1(arr):
    """Works but I'm guessing this is basic"""
    v2 = np.prod(arr)
    answer =v2 / arr
    return answer

def v2(arr):
    """same thing as v1 but without numpy"""
    v2 = math.prod(arr)
    answer = [int(v2 / element) for element in arr]
    return answer

def bonusv2(arr):
    prod = [1] * len(arr)

    for i in range(1, len(arr)):
        prod[i] *= prod[i - 1] * arr[i - 1]
    print(prod)

    backwards = 1
    for j in range(len(arr) - 2, -1, -1):
        backwards *= arr[j + 1]
        prod[j] *= backwards 
    print(prod)

#a1 = np.flip(np.arange(1, 4))
#v1 works

inc = [*range(1,6)]
# v2 works
yayo = math.prod(inc)

#playing around with no div method
print(yayo)

print(inc)
bonusv2(inc)