from math import prod

def pain(chart, length):
    answer = 0
    for arr in range(len(datalist)):
        for num in range(len(datalist[arr])):
            
            if(num + length >= len(datalist[arr]) or 
            arr + length >= len(datalist)):
                continue

            #horizontal
            horiz = datalist[arr][num: num + length]
            h = prod(horiz)

            #vertical
            vert = [datalist[arr + i][num] for i in range(length)]
            lil_uzi = prod(vert)


            #negative slope diagonal
            negDiag = [datalist[arr + i][num - i] for i in range(length)]
            nd = prod(negDiag)

            #positive slope diagonal
            posDiag = [datalist[arr + i][num + i] for i in range(length)]
            pd = prod(posDiag)

            answer = max(h, lil_uzi, nd, pd, answer)
    return answer

datalist = []
with open("Problem11\\num.txt") as f:
    for line in f:
        line = line.rstrip()
        line_list = list(line.split())
        datalist.append([int(i) for i in line_list])

print(pain(datalist, 4))

# #horizontal
#             temp = datalist[arr][num - length: num]
#             yayo = prod(temp)
            
#             answer = max(answer, yayo)

#             # vertical
#             temp = [datalist[arr - i][num] for i in range(0,length)]
#             yayo = prod(temp)
            
#             answer = max(answer, yayo)

#             #upright
#             if(arr + length <= len(datalist) and 
#             num + length <= len(datalist[arr])):

#                 print(arr)

#                 temp = [datalist[arr + i][num - i] for i in range(0,length)]
#                 yayo = prod(temp)
                
#                 answer = max(answer, yayo)

#                 temp = [datalist[arr + i][num + i] for i in range(0,length)]
#                 yayo = prod(temp)
                
#                 answer = max(answer, yayo)