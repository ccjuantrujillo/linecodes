def concatena_seis_veces(lista):
    resultado=lista
    for i in range(5):
        resultado = resultado + lista

    return resultado

print concatena_seis_veces('edward')