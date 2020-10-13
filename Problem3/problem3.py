import math


def primefactorization(number):
    primes = []
    if number %2 == 0:
        primes.append(2)
        while number % 2 == 0:
            number /= 2
    for i in range(3, int (math.sqrt(number)) + 1, 2):
        if number % i == 0:
            primes.append(i)
            while number % i == 0:
                number /= i

    return primes[len(primes) - 1]

print(primefactorization(600851475143 ))