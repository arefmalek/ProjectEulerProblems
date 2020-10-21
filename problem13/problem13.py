def summing(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            total += int(line)

    return str(total)[:10]

print(summing("number.txt"))
