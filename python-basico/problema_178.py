cadena = raw_input('Escribe una frase: ')

#elimina los espacios en blanco a la izquierda y a la derecha
filtrado = cadena.strip()

resultado_1 = 0
resultado_2 = 0

for aux in range(0,len(filtrado.split())):
    for var in range(0,len(filtrado.split()[aux])):
        if filtrado.split()[aux][var:var+1] == '(':
            resultado_1 = resultado_1 + 1
        if filtrado.split()[aux][var:var+1] == ')': 
            resultado_2 = resultado_2 + 1

print resultado_1
print resultado_2

if resultado_1 == resultado_2:
    print 'La cadena esta bien parentizada'
else:
    print 'La cadena no esta bien parentizada'    

    