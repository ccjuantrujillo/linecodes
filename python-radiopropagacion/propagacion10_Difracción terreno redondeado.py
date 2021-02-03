#Calcula difracción para terreno redondeado en función de f, d1, d2, h y R
import math

frec = float(input('Frecuencia f(Mhz): '))
d1   = float(input('Distancia d1(km): '))
d2   = float(input('Distancia d2(km): '))
h    = float(input('Altura del obstáculo h(m): '))
R    = float(input('Radio de la tierra R(km): '))

#Calculos
c   = 3e+8
l   = c/(frec*1e+6)
v   = h*math.sqrt((2/l)*(1/(d1*1000) + 1/(d2*1000)))
Ld  = 6.9 + 20*math.log10(math.sqrt(pow(v-0.1,2) + 1) + v - 0.1)
m   = R*((d1+d2)/(d1*d2))/pow(math.pi*R/l,1/3)
n   = h*math.pow(math.pi*R/l,2/3)/R
k   = 8.2 + 12*n
b   = 0.73 + 0.24*(1 - math.exp(-1.43*n))
Tmn = k*pow(m,b)

#Mostramos resultados
print('\nVariable v = ',v)
print('Perdida J(v)(dB) = ', -Ld)
print('Variable m = ',m)
print('Variable m = ',n)
print('Perdida T(m,n)(dB) = ', -Tmn)