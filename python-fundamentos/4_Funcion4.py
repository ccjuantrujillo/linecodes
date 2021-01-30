#suma_lista
def sumatorio(lista):
    s = 0
    for numero in lista:
        s += numero
    return s

a = [1,2,3]

print sumatorio(a)

print sumatorio([1,2,3,4])

