#cadena = 'edward'
#print cadena[0]

def nombres_con_letra(lista,caracter):
    resultado = []
    for elemento in lista:
        if elemento[0] == caracter:
            resultado.append(elemento)

    return resultado

print nombres_con_letra(['edward','edu','alexander'],'e')
