from itertools import permutations

UPPER_LIMIT = 9

x = [*range(0,UPPER_LIMIT + 1)]

copies = [subset for subset in permutations(x,UPPER_LIMIT + 1)]

answer = 0
for i in copies[999_999]:
    answer *=10
    answer += i

print(answer) # I was too lazy to just type out the stuff from belows
print(copies[999_999])
