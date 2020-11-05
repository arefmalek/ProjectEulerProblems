import numpy as np

def factorize(n):
    ind = 1
    fac_count = 1
    while fac_count < n_count:
        ind+=1
        num = sum(range(ind + 1))
        factors = []
        for i in range(1, int(num**0.5 + 1)):
            if (num % i == 0):
                if (i == num ** 0.5):
                    factors.append(i)
                else:
                    factors.extend([i, int(num / i)])
        fac_count = len(factors)

    return (sum(range(ind + 1)))

n_count = 500
print(factorize(n_count))

