def sin_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def comunes_dos_listas(lista1,lista2):
    resultado = []
    for elemento in lista1:
        for elemento_2 in lista2:
            if elemento == elemento_2:
                resultado.append(elemento)

    salida = sin_repetidos(resultado)
    return salida


print comunes_dos_listas([1,2,1,4,3,5,7,5,4,4],[2,3,2,4,5,7,8,6,9,7,5,4])
                
                
    