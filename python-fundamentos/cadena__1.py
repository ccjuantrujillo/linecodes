#subcadena
cadena = raw_input('Dame una cadena: ')

i = int(raw_input('Dame un numero: '))
j = int(raw_input('Dame otro numero: '))

if i < 0:
    inicio = 0
else:
    inicio = i

if j > len(cadena):
    final = len(cadena)
else:
    final = j

subcadena = ''

for k in range(inicio,final):
    subcadena = subcadena + cadena[k]

print 'La subcadena entre %d y %d es %s, ' %(i,j,subcadena)


