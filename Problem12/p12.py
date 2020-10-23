import numpy as np

def tryit(aye):
    triangle = sum(range(1, aye + 1))
    factors = [triangle]

    for num in range(1, int(triangle/2) + 1):
        if (triangle%num == 0):
            print(num)
            factors.append(num)


print(tryit(7))