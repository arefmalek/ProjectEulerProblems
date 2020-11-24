import sys

def fibs(fprev, fnow, index = 1):
    """lol went too high up the recursive stack"""
    fyes = fnow + fprev

    index += 1
    if (len(str(fyes)) < 1000): 
        return fibs(fnow, fyes, index=index)
    else: return index

def nonRecurse(limit):
    fprev = 0
    fnow = 1
    index = 1
    
    while len(str(fprev + fnow)) < limit:
        temp = fnow
        fnow += fprev
        fprev = temp
        index += 1
    
    index += 1
    return index

print(nonRecurse(1000))