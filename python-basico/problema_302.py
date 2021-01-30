from random import random

def aleatorio():
    x = -10
    y = 10

    return int(x + (y-x+1)*random())


print aleatorio()