cadena = raw_input('Escribe una frase: ')

salida = ''

for variable in range(0,len(cadena.split())):                      
    for var in range(0,len(cadena.split()[variable])):
        if cadena.split()[variable][var:var+1] != '1' and cadena.split()[variable][var:var+1] != '2' and cadena.split()[variable][var:var+1] != '3' and cadena.split()[variable][var:var+1] != '4' and cadena.split()[variable][var:var+1] != '5' and cadena.split()[variable][var:var+1] != '6' and cadena.split()[variable][var:var+1] != '7' and cadena.split()[variable][var:var+1] != '8' and cadena.split()[variable][var:var+1] != '9':
            salida = salida + ' '
        else:
            salida = salida + cadena.split()[variable][var:var+1]
    salida = salida + ' '
#cadena.strip() quita espacios en blanco en izquierda y derecha    
#print salida[0]
#print salida[1]
#print salida[2]
filtrado = salida.strip()

print filtrado.split()

print 'La cantidad de numeros ingresados:',len(filtrado.split())

print 'Los numeros son los siguientes:'

for aux in range(0,len(filtrado.split())):
    print filtrado.split()[aux]