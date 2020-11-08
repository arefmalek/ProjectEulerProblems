from math import log2

def calc_sequence(n, cap = 1_000_000):

    total_calcs = 1
    while (n != 1):
        if n >= cap:
            return total_calcs

        if (n % 2 == 1):
            n = 3 * n + 1
        else:
            n/=2
        total_calcs += 1

    return(total_calcs)

def recurse(entire_array, ind):
    print(ind)
    
    if ind % 2 == 1:
        print("odd")
        temp = 3*ind+1
    else:
        print("even")
        temp = ind/2
    
    if (temp == 1):
        print("done")
        return
    temp = (int(temp))
    
    recurse(entire_array, temp)

    entire_array[ind][0] = entire_array[temp][0] + 1        

yeet = [[i, 0] for i in range(1, 50)]
yeet[0][1] = 1
print(recurse(yeet, 13))