cadena = str(raw_input('Ingrese una cadena: '))

var = len(cadena)

print 'la longitud es:',var

#for var in range(1,len(cadena)+1):
#    print cadena[0:var]

#print cadena[0:3]
#print cadena[1:4]
#print cadena[2:5]
#print cadena[3:6]

for var in range(0,len(cadena)-2):
    print cadena[var:var+3]
