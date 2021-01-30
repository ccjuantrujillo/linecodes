cadena = raw_input('Escribe una frase: ')
k = int(raw_input('Ingrese el numero para buscar palabras largas: '))
cambios = 0
contador = 0
salida = 0
palabras = 0
for caracter in cadena:
    contador = contador + 1
    if caracter == ' ':        
        cambios += 1
        

palabras = cambios + 1

#print 'Cantidad de palabras en la oracion:',palabras
#print 'longitud de la variable',len(cadena)
#print 'una parte de la cadena',cadena[1:4]

for palabra in range(0,palabras):
    if len(cadena.split()[palabra]) >= k:
        salida = salida + 1        

if salida == 0:
    print 'No hay palabras largas'
else:
    print 'Hay palabras largas'