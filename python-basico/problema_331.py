def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def union_de_listas(lista1,lista2):
    resultado = []
    for elemento1 in lista1:
        resultado.append(elemento1)
    for elemento2 in lista2:
        resultado.append(elemento2)

    salida = sin_repetidos(resultado)
    return salida

print union_de_listas([1,2,1],[2,3,2])
        
        