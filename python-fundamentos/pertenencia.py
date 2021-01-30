##elemento = 5
##lista = [1,4,5,1,3,8]
##
##pertenece = False
##
##for i in lista:
##    if elemento == i:
##        pertenece = True
##        break
##
##if pertenece:
##    print 'Pertenece'
##else:
##    print 'No Pertenece'    

##conjunto = [1,2,3]
##
##elemento = int(raw_input('Dame un numero: '))
##
##if not elemento in conjunto:
##    conjunto.append(elemento)
##

conjunto = [1,2,3]

elemento = int(raw_input('Dame un numero: '))

if elemento not in conjunto:
    conjunto.append(elemento)

print conjunto
