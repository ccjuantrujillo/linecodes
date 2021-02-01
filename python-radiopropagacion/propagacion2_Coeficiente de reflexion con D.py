import cmath
import math
import numpy

print('Calculo del coeficiente de reflexión R con Divergencia: ')
print('======================================================= ')
R     = float(input('Coeficiente de reflexion |R|: '))
betha = float(input('Angulo de reflexion β(ºC): '))
D     = float(input('Coeficiente de divergencia D: '))
sigma = float(input('Rugosidad del terreno σc: '))
phi   = float(input('Angulo de incidencia φ (ºC): '))
dt    = float(input('Diferencia de fase Δθ(rad): '))
frec  = float(input('Frecuencia (Mhz): '))
d  = float(input('Distancia del enlace d (km): '))

c   = 3e+8
l   = c/(frec*1e+6)
gm  = 4*math.pi*sigma*numpy.sin(math.radians(phi))/l
Rd  = R*D*math.exp(-gm*gm/2)
df  = dt%(2*math.pi)+math.pi+betha*math.pi/180
lbf = 20*math.log(4*math.pi*d*1000/l,10)
lb  = lbf - 10*math.log(1 + pow(D*R,2) + 2*D*R*math.cos(df) ,10)

print('\nCoef. de reflexion con divergencia Rd = ',Rd)
print('Angulo de desfasamiento Δ(rad) = ',df)
print('Pérdida de propagación Lb(db) = ',lb)
