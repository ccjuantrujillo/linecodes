cadena = str(raw_input('Ingrese una cadena: '))

auxiliar = cadena.lower()

salida = auxiliar.split()

#print salida[1]
#print len(salida)

print len(salida)

for aux in range(0,len(salida)-2):
    if salida[aux] == salida[aux+1]:
        del salida[aux+1]

if salida[len(salida)-2] == salida[len(salida)-1]:
    del salida[len(salida)-1]

print salida