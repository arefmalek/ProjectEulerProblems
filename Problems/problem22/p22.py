with open("problem22/names.txt") as f:
    yeah = f.read().split('","')
    yeah[0] = yeah[0].lstrip('"')
    yeah[len(yeah) - 1] = yeah[len(yeah) - 1].rstrip('"')
    yeah = sorted(yeah)

# A = 65
answer = 0
for i in range(len(yeah)):
    swag = [ord(c) - 64 for c in yeah[i]]
    answer += (i + 1) * sum(swag)
print(answer)