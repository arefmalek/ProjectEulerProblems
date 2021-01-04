from itertools import combinations

def abundant(number):
    """returns the sum of factors if abundant, 
    otherwise returns 0"""
    factors = 1
    for i in range(2, int(number ** 0.5 + 1)):
        if (number % i == 0):
            if (i == number ** 0.5): factors += i
            else: factors += i + (number / i)    
    return number if factors > number else 0



x = [i for i in range(1,28123) if abundant(i) > 0]

copies = {sum(subset) for subset in combinations(x,2) if sum(subset) < 28123}
copies.update({2*z for z in x if 2*z < 28123})

answers = [i for i in range(1,28123) if i not in copies]
print(sum(answers))
