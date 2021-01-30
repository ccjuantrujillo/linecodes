#Area con formato
from math import pi

radio = float(input('Dame el radio '))

area = pi * radio**2

print ('El area de un circulo de radio %f es %f' % (radio,area))

print ('El area de un circulo de radio %6.3f es %6.3f' % (radio,area))


