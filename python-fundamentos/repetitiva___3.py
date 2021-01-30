#raiz
from math import sqrt
x = -1
while x < 0:
    x = float(raw_input('Introduce un numero positivo'))

print 'La raiz cuadrada de %f es %f' % (x,sqrt(x))
