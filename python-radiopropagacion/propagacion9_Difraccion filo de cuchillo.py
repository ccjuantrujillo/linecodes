#Calcula difracción por filo de cuchillo en función de f, d1, d2 y h
import math

frec = float(input('Frecuencia f(Mhz): '))
d1   = float(input('Distancia d1(km): '))
d2   = float(input('Distancia d2(km): '))
h    = float(input('Altura del obstáculo h(m): '))

#Calculos
c  = 3e+8
l  = c/(frec*1e+6)
v  = h*math.sqrt((2/l)*(1/(d1*1000) + 1/(d2*1000)))
Ld = 6.9 + 20*math.log10(math.sqrt(pow(v-0.1,2) + 1) + v - 0.1)

#Mostramos resultados
print('\nVariable v = ',v)
print('Perdida J(v)(dB) = ', -Ld)