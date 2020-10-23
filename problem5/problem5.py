import numpy as np


# thought design:
#
# multiply all numbers together
# figure out a way that every number that is multiple of two prime numbers
# already in the list get removed from the list

def donesos(limit):
    primeList = sieve(limit)
    number = np.prod(primeList)

    #ok wait i understand now
    #so basically it has to be divisible by the largest number
    #and all other numbers don't really matter
    #you're bound to get something that fits all the other points we mentioned earlier
    #but we can guarantee that happens the fastest by adding the largest prime in the multiple
    #regardless of what we do, smallest num divisible by all vals gotta be div by prime numbers too
    while(process(limit, number) != 0):
        number += primeList[len(primeList) - 1]

    return number

def process(limit, number):

    for i in range(limit, int(limit/2), -1):
        if number%i != 0:
            return 1
    #congrats!
    return 0


def sieve(number):
    answer = []
    plist = [True] * number
    for i in range(2, number):
        if plist[i]:
            answer.append(i)
            for j in range(i*i, number, i):
                plist[j] = False

    return answer

print(donesos(20))