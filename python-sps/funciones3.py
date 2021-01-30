def doble(x):
    return 2*x

def main(f):
    return f(4)


doble(2)
doble(5)

var = doble

print(main(doble))
