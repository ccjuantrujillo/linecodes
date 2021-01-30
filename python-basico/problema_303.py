from random import random

def dado():
    x = 1
    y = 6

    return int(x + (y-x+1)*random())


print dado()