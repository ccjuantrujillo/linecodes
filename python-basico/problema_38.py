from math import sin

lado_1 = float(raw_input('Ingrese el valor de una lado: '))

lado_2 = float(raw_input('Ingrese el valor del otro lado: '))

angulo = float(raw_input('Ingrese el angulo que forman los lados: '))

angulo_radian = float(angulo * ( 3.1416 / 180))

area = lado_1 * lado_2 * sin(angulo_radian) * 0.5

print 'El area del triangulo es:',area,'...' 

