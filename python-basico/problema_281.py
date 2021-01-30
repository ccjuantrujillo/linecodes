def media_lista(lista):
    if len(lista) > 0:
        suma = sum(lista)
        var = len(lista)
        resultado = 1.0*suma/var
    else:
        resultado = 0
    return resultado

print media_lista([1,2,3,2,3,4,4,3,2,2,12,0.655])

    