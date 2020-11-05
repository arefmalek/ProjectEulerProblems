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

#a1 = np.flip(np.arange(1, 4))
#v1 works

inc = [*range(1,6)]
# v2 works
yayo = math.prod(inc)

#playing around with no div method
print(yayo)

answer = [i for i in inc]
print(inc)
print(answer)
