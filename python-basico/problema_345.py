from math import *

def abslista(lista):
    for i in range(len(lista)):
        lista[i] = abs(lista[i])

milista = [1,-1,2,-3,-2,0]

abslista(milista)

print milista