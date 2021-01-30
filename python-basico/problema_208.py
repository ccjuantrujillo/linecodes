cadena1 = str(raw_input('Ingrese una primera cadena: '))
cadena2 = str(raw_input('Ingrese una segunda cadena: '))

#for var in range(1,len(cadena)+1):
#    print cadena[0:var]

#print cadena[0:3]
#print cadena[1:4]
#print cadena[2:5]
#print cadena[3:6]

salida = 0

for aux in range(0,len(cadena1)):
    for var in range(0,len(cadena1)-2):
        if cadena1[var:var+aux] == cadena2:
            salida = 1                


if salida == 0:
    print 'Una cadena no es prejifo de otra'
if salida == 1:
    print 'Una cadena si es prejifo de otra'    
    