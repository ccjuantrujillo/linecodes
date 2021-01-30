cadena1 = str(raw_input('Ingrese una primera cadena: '))
cadena2 = str(raw_input('Ingrese una segunda cadena: '))
cadena3 = str(raw_input('Ingrese una tercera cadena: '))

limite = len(cadena1)

if limite > len(cadena2):
    limite = len(cadena2)
if limite > len(cadena3):
    limite = len(cadena3)   

salida = ''


for var in range(0,limite):
    if cadena1[var:var+1] == cadena2[var:var+1] and cadena2[var:var+1] == cadena3[var:var+1]:
        salida = salida + cadena1[var:var+1]
    else:
        break

if len(salida) == 0:
    print 'Las tres cadenas no tienen prefijo comun'
else:
    print 'El prefijo comun mas largo es:',salida

#invertir una cadena c[::-1]