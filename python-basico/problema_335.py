def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def es_primo(numero):
    s = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            s = s + 1
            
    if s == 2:
        return True
    else:
        return False



def solo_primos(lista):
    resultado = []
    for elemento in lista:
        if es_primo(elemento):
            resultado.append(elemento)

    salida = sin_repetidos(resultado)
    return salida

print solo_primos([3,2,3,4,32,34,4,6,6,7,8,7,5,54,67,8,9,7,6,54,34,3,2])




