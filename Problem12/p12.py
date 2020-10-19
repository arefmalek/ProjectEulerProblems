#work backwards, give in input number, return list of divisors

#screw it im bruce forcing lol

def triangle(number):

    guys = [*range(1, number+1)]
    total = sum(guys)

    factors = []
    for i in range(1, int(total/2)):
        if(total % i == 0):
            factors.append(i)
    factors.append(number)
    return len(factors), total

i = 0
divisors, tri_num = triangle(i)
while (divisors < 500):
    divisors, tri_num = triangle(i)
    i+=1

print(tri_num)
