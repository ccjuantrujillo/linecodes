import cmath
import math
import numpy

print('Calculo del coeficiente de reflexión R: ')
print('======================================= ')
frec  = float(input('Frecuencia (Mhz): '))
theta = float(input('Angulo de incidencia φ (ºC): '))
er    = float(input('Permitividad relativa εr: '))
sigma = float(input('Conductividad del medio σ: '))

print('\na) Longitud de onda λ (m): ')
c = 3e+8
l = c/(frec*1e+6)
print('λ (m) = ',l)

print('\nb) Constante dieléctrica compleja de la tierra εc: ')
ec  = er - 60*sigma*l*1j
(r, phi) = cmath.polar(ec)
print('εc = ',ec)
print('|εc| = ',r,', θ = ',phi*180/math.pi)

print('\nc) Impedancia horizontal Zh (Ω): ')
Zh = numpy.sqrt(ec - pow(math.cos(math.radians(theta)),2))
(r, phi) = cmath.polar(Zh)
print('Zh (Ω) = ',Zh)
print('|Zh| = ',r,', θ = ',phi*180/math.pi)

print('\nc) Impedancia vertical Zv (Ω): ')
Zv = numpy.sqrt(ec - pow(math.cos(math.radians(theta)),2))/ec
(r, phi) = cmath.polar(Zv)
print('Zv (Ω) = ',Zv)
print('|Zv| = ',r,', θ = ',phi*180/math.pi)

print('\nd) Coeficiente de reflexión horizontal Rh : ')
Rh = (math.sin(math.radians(theta)) - Zh)/(math.sin(math.radians(theta)) + Zh)
(r, phi) = cmath.polar(-Rh)
print('Rh  = ',Rh)
print('|Rh| = ',r,', β = ', -phi*180/math.pi)

print('\nd) Coeficiente de reflexión vertical Rv : ')
Rv = (math.sin(math.radians(theta)) - Zv)/(math.sin(math.radians(theta)) + Zv)
(r, phi) = cmath.polar(-Rv)
print('Rv  = ',Rv)
print('|Rv| = ',r,', β = ', -phi*180/math.pi)

