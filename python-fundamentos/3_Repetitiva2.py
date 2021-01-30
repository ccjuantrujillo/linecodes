#circulo
from math import pi



opcion = ''

while opcion != 'd':
    radio = float(raw_input('Dame el radio de un circulo: '))
    print 'Escoge una opcion:'
    print 'a) Calcular el diametro.'
    print 'b) Calcular el perimetro.'
    print 'c) Calcular el area.'
    print 'd) Finalizar.'

    opcion = raw_input('Teclea a, b o c y pulsa el retorno de corro: ')

    if opcion == 'a' or opcion == 'A' :
        diametro =  2 * radio
        print 'El diametro es:',diametro

    elif opcion == 'b' or opcion == 'B' :
        perimetro = 2 * pi * radio
        print 'El perimetro es:',perimetro

    elif opcion == 'c' or opcion == 'C':
        area = pi * radio**2
        print 'El area es:',area
    elif opcion == 'd' or opcion == 'D':
        print 'Solo hay tres opciones: a, b o c'
        print 'Tu has tecleado ',opcion

print 'Gracias por usar este prgrama'           
        

