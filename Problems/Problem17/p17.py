ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
             "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ",
             "novemdecillion ", "vigintillion "]

def printNum(number):
    pog = ""
    one = int(number % 10)
    tens = int(number % 100 - one)
    hundreds = int(number / 100)

    if (0 < hundreds < 10):
        pog += ones[hundreds] + "hundred "
        if (tens == 0 and one == 0):
            print("SKIP")
        else: pog += "and "

    if (tens < 20):
        pog += ones[tens + one]
    else:
        pog += twenties[int(tens/10)] + ones[one]

    return pog


sum = 0
for i in range(1, 1000):
    a = printNum(i).replace(" ", "")
    print(a)
    sum += len(a)

sum += len("one thousand".replace(" ", ""))
print(sum)