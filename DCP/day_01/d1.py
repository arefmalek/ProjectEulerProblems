def poggers(array, k):
    for num in array:
        diff = k - num
        if diff in array:
            return True

z = [10, 15, 3, 7]
print(poggers(z, 17))