cadena = str(raw_input('Ingrese una cadena: '))

var = len(cadena)

print 'la longitud es:',var

for var in range(1,len(cadena)+1):
    print cadena[0:var]




