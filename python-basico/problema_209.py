cadena1 = str(raw_input('Ingrese una primera cadena: '))
cadena2 = str(raw_input('Ingrese una segunda cadena: '))

if len(cadena1) > len(cadena2):
    limite = len(cadena2)
else:
    limite = len(cadena1)   

salida = ''


for var in range(0,limite):
    if cadena1[var:var+1] == cadena2[var:var+1]:
        salida = salida + cadena1[var:var+1]
    else:
        break

if len(salida) == 0:
    print 'Las dos cadenas no tienen prefijo comun'
else:
    print 'El prefijo comun mas largo es:',salida