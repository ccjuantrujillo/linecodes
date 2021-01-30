cadena = raw_input('Escribe una frase: ')
k = int(raw_input('Ingrese la longitud de la cadena a buscar: '))
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
    if len(cadena.split()[palabra]) == k:
        salida = salida + 1        

if salida == palabras:
    print 'Todas las palabras tienen longitud',k
else:
    print 'No todas las palabras tiene longitud',k