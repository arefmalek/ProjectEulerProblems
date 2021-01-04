def powerSum(base, exponent):
    total = 0
    num = str(base ** exponent)

    for i in num:
        total += int(i)

    return total

print(powerSum(2, 1000))