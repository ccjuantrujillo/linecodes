#list[::-1]

cadena = raw_input('Introduce una cadena: ')

inversion = ''

for variable in range(0,len(cadena.split())):
    inversion = inversion + cadena.split()[variable]


if inversion == inversion[::-1]:
    print 'La frase es palindroma'
else:
    print 'La frase no es palindroma' 
