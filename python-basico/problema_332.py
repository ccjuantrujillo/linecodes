def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def diferencia_de_listas(lista1,lista2):
    resultado = []
    for elemento in lista1:
        if (elemento in lista1) and (elemento not in lista2):
            resultado.append(elemento)

    salida = sin_repetidos(resultado)
    return salida

print diferencia_de_listas([1,2,1],[2,3,2,4])

