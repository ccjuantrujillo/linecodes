def cadena_mas_larga(lista):
    B=[]
    for i in range(len(lista)):
        B.append(len(lista[i]))
        
    resultado = max(B)
    for i in range(len(B)):
        if resultado == B[i]:
            salida = i
            break

    return lista[salida]

print cadena_mas_larga(['edward','alexander','karin','betsy','ejemplo largo'])
        