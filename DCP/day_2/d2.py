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

    backwards = 1
    forwards = 1

    for i in range(1, len(arr)):
        print(forwards, backwards)
        print(prod)

        forwards *= arr[i - 1]
        prod[i] *= forwards 
        #messy I know but I really want this in one loop
        
        n = len(arr) - 1 - i
        backwards *= arr[n + 1]
        prod[n] *= backwards
    print(forwards, backwards)

    return(prod)

inc = [3, 6, 2, 5, 4]
# v2 works
yayo = math.prod(inc)
print(yayo)
print(inc)
print(bonusv2(inc))

print(v2(inc))