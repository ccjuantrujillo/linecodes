def invierte(lista):
    for i in range(len(lista)/2):
        c = lista[i] 
        lista[i] = lista[-i-1]
        lista[-i-1] = c

a = [1,2,3,4]

invierte(a)

print a
