import numpy as np

def triple(limit):
    for a in range (1, limit):
        for b in range (a + 1, limit):
            c = b + 1

            while (c ** 2 < a ** 2 + b ** 2):
                c+=1

            if (a **2 + b **2 == c**2):
                    print(a, b, c)

                    result = limit / (a + b + c)
                    if (result % 1 == 0):
                        return(result ** 3 * a * b * c)
                



print(triple(1000))