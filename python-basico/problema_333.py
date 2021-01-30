def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def solo_pares(lista):
    resultado = []
    for i in lista:
        if i%2 == 0:
            resultado.append(i)

    salida = sin_repetidos(resultado)
    return salida

print solo_pares([2,4,6,1,3,5,7])
            
        
        