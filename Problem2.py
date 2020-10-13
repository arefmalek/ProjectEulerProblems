numbers = [0,1]
answer = 0

while sum(numbers) < 4_000_000:
    temp = sum(numbers)
    numbers[0] = numbers[1]
    numbers[1] = temp
    if temp %2 == 0: answer += temp

print(answer)