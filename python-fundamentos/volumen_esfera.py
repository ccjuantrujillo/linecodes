from math import pi

print 'Programa para el calculo del volumen de una esfera'

radio = float(raw_input('Dame el radio: '))

volumen = (4.0/3.0) * pi * radio**3

print 'Volumen de la esfera:' ,volumen, 'metros cubicos'