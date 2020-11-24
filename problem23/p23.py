from itertools import combinations

def abundant(number):
    """returns the sum of factors if abundant, 
    otherwise returns 0"""
    factors = 1
    for i in range(2, int(number ** 0.5 + 1)):
        if (number % i == 0):
            if (i == number ** 0.5): factors += i
            else: factors += i + (number / i)    
    return int(factors) if factors > number else 0

def gf(num):
    """this has nothing to do with the problem,
    I just realized modeling factorials was easier than
    expected"""
    if(num == 1): return num
    return (num * gf(num - 1))

def combos(nums):
    """kinda cheating cuz im using builtins"""
    answers = list(set([sum(comb) for comb in combinations(nums, 2) 
    if sum(comb) < 28123]))

    return answers




abundants = [abundant(i) for i in range(11, 28123) if 28123 > abundant(i) > 0]

ans = combos(abundants)
print(len(ans))