from math import factorial

# thought design:
#
# multiply all numbers together
# figure out a way that every number that is multiple of two prime numbers
# already in the list get removed from the list

def multiplier(number):
    total = factorial(number)

    squa = [*range(1, number + 1)]

    for i in range(number, 1, -1):
        total /= i
        print(i)

        for j in range(1, i):
            if i % j == 0 and j in squa:
                squa.remove(j)


    return squa


print(multiplier(10))