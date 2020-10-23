def triplet(n):
    for x in range(1, n):
        for y in range((x+1), n):
            for z in range((y+1), n):
                if x ** 2 == y ** 2 + z ** 2:
                    print(y, z, x)
                    print('/' * 50)

triplet(1000)