def squareDifference(number):
    something = [*range(1, number + 1)]
    total = 0

    for nums in something:
        total += nums**2
    second = (number*(number + 1)/2)**2
    return second - total

print(squareDifference(100))