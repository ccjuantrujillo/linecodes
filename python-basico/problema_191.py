#list[::-1]

cadena = raw_input('Introduce una cadena: ')

inversion = ''

for caracter in cadena:
    inversion = caracter + inversion

if cadena == inversion:
    print 'La palabra es palinbroma'
else:
    print 'La palabra no es palinbroma'    
