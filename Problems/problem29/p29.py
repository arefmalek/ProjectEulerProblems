def p29(limit):
    terms = set()

    for a in range(2, limit + 1):
        for b in range(2,limit + 1):
            terms.add(a**b)
    
    return len(terms)

print(p29(100))