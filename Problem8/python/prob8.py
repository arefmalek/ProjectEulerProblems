from math import prod

def fmlfmlfml(lepsis, length):
    answer = 0
    for i in range(len(lepsis) - length):
        temp = lepsis[i:i+length]
        yayo = prod(temp)
        answer = max(answer, yayo)
    return answer

datalist = []
with open("Problem8\\num.txt") as f:
    for line in f:
        #line = line.replace(" ", "")
        datalist.extend(list(line.strip('\n')))
        # line_list = list(line.strip('\n'))
        # datalist.append(int(i) for i in line_list)
    datalist = [int(i) for i in datalist]

print(fmlfmlfml(datalist, 13))