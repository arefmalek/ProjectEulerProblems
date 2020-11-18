def factorize(num):
    factors = [1]
    for i in range(2, int(num**0.5 + 1)):
        if (num % i == 0):
            if (i == num ** 0.5):
                factors.append(i)
            else:
                factors.extend([i, int(num / i)])
    return(factors)
    
def organize(num):
    return (sum(factorize(num)))

def amicable(limit):
    skippers = []
    amics = []
    for i in range(2, limit + 1):
        if (i in skippers): continue

        if (i == organize(organize(i))):
            if (i == organize(i)): continue
            else: amics.extend([i, organize(i)])
            skippers.append(organize(i))
    return(amics)


print(sum(amicable(10_000)))