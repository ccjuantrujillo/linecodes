#maximo
def maximo(lista):
    if len(lista)>0:
        candidato = lista[0]
        for elemento in lista:
            if elemento > candidato:
                candidato = elemento
    else:
        candidato = None
    return candidato

print maximo([6,2,7,1,10,1,0])
        