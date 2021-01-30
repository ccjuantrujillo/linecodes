a = int(raw_input('Ingrese el primer numero'))
b = int(raw_input('Ingrese el segundo numero'))

num = a**2

if b == num:
    print 'El segundo es el cuadrado perfecto del primero'
if b < num:
    print 'El segundo es menor que el cuadrado perfecto'
if b > num:
    print 'El segundo es mayor que el cuadrado perfecto'
