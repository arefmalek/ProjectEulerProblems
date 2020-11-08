def v1(arr):
    pog = [*range(1, max(arr))]
    if (pog in arr):
        return max(arr) + 1

    for i in pog:
        if (i not in arr):
            return i

def v2(arr):
    # arr.sort()

    # arr = [i for i in arr if (i > 0)]
    # print(arr)

    for i in range(1, len(arr)):
        if (i not in arr):
            return i

    return len(arr) + 1

print(v2(
    [3, 4, -1, 1]
))