def spiral(n):
    if (n == 1):
        return 1

    sum = 0
    for i in range(n**2 - 3 * (n-1), n**2 + 1, (n-1)):
        sum += i
    
    return spiral(n-2) + sum

print(spiral(1001))