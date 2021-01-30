from math import pi

radio = float(raw_input('Ingrese el radio: '))

perimetro = 2.0 * pi * radio

area = pi * radio**2

print 'La circunferencia con radio %3.2f tiene el siguiente perimetro %.2f y el area %.2f' % (radio,perimetro,area)

