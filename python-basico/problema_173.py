cadena = raw_input('Escribe una frase: ')
#k = int(raw_input('Ingrese el numero para buscar palabras largas: '))
cambios = 0
contador = 0
salida = 0
palabras = 0
for caracter in cadena:
    contador = contador + 1
    if caracter == ' ':        
        cambios += 1
        

palabras = cambios + 1

#print 'Cantidad de palabras en la oracion:',len(cadena.split())
#print 'longitud de la variable',len(cadena)
#print 'una parte de la cadena',cadena[1:4]

##for palabra in range(0,palabras):
##    if len(cadena.split()[palabra]) >= k:
##        salida = salida + 1        
##
##if salida == palabras:
##    print 'Todas las palabras son largas'
##else:
##    print 'Hay alguna palabra corta'
resultado = 0
for variable in range(0,len(cadena.split())):                      
    for var in range(0,len(cadena.split()[variable])):
        if cadena.split()[variable][var:var+1] == '1' or cadena.split()[variable][var:var+1] == '2' or cadena.split()[variable][var:var+1] == '3' or cadena.split()[variable][var:var+1] == '4' or cadena.split()[variable][var:var+1] == '5' or cadena.split()[variable][var:var+1] == '6' or cadena.split()[variable][var:var+1] == '7' or cadena.split()[variable][var:var+1] == '8' or cadena.split()[variable][var:var+1] == '9':
            resultado = resultado + 1
                    
print 'La cantidad de digitos presentes es',resultado    