cadena = raw_input('Dame una cadena: ')

i = int(raw_input('Dame un numero: '))
n = int(raw_input('Dame otro numero: '))

subcadena = ''

for k in range(i,i+n):
    subcadena = subcadena + cadena[k]

print 'La subcadena es:',subcadena
