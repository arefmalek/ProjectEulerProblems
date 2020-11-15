def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    
    return

x = cons(1, 3)
print(car(x))