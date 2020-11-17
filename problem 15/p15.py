from math import factorial

def neLatticePath(number):
    return(factorial(2 * number) / (factorial(number)**2))

print(neLatticePath(20))