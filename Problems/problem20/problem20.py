from math import factorial

def factSum(number):
    factString = str(factorial(number))
    factArr = [int(i) for i in factString]
    return(sum(factArr))

print(factSum(100))