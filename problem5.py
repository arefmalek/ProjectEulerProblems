# thought design:
#
# multiply all numbers together
# figure out a way that every number that is multiple of two prime numbers
# already in the list get removed from the list

def multiplier(number):
    num = [*range(3, number, 2)]
    remaining = []


answer = 1
for x in range(2, 21):
    answer *= x
print(answer)
