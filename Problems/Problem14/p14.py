from math import log2

def recurse(ind, iteration_counts=0):

    if (ind == 1):
        iteration_counts += 1
        return iteration_counts
    elif ind % 2 == 1:
        temp = 3*ind+1
    else:
        temp = ind/2
    

    temp = (int(temp))
    iteration_counts +=1
    return recurse(temp, iteration_counts)

arr = [recurse(i) for i in range(1, 1_000_000)]

print(arr.index(max(arr)) + 1)