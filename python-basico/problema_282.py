def producto_lista(lista):
    producto = 1    
    if len(lista) > 0:
        for i in lista:
            producto = producto * i
    else:
        producto = 0
    return producto

print producto_lista([1,2,3,4])
