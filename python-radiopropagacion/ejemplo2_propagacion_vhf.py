import cmath
import math
import numpy

print('Propagación en la tropósfera: ')
print('============================ ')
ht = float(input('Horizonte de la antena transmisora ht (m): '))
hr = float(input('Horizonte de la antena receptora hr (m): '))
d  = float(input('Distancia del enlace d (km): '))
k  = float(input('Constante k: '))
f  = float(input('Frecuencia (Mhz): '))
pol  = int(input('Polarización vertical V (1), polarización horizontal H (2): '))

print('\na) Longitud de onda λ (m): ')
c = 3e+8
l = c/(f*1e+6)
print('λ (m) = ',l)

print('\nb) Parametro p: ')
p = (2/numpy.sqrt(3))*numpy.sqrt(6.37*k*(ht+hr) + pow(d/2,2))
print('p = ',p)

print('\nc) Parametro α ')
theta = math.acos(12.74*k*(ht-hr)*d/pow(p,3))
print('α = ',theta*180/math.pi)

print('\nd) Parametro d1 y d2 (km): ')
d1 = (d/2) + p*math.cos((math.pi+theta)/3)
d2 = d - d1
print('d1 (km) = ',d1)
print('d2 (km)= ',d2)

print("\ne) Parametro ht' y hr' (m): ")
Re  = 6370
htp = ht - pow(d1,2)*1000/(2*k*Re)
hrp = hr - pow(d2,2)*1000/(2*k*Re)
print("ht' (m) = ",htp)
print("hr' (b)= ",hrp)

print("\nf) Angulo adyacente φ (mrad): ")
ang = math.atan((htp + hrp)/(d*1000))
print("φ (mrad)' = ",ang*1000)
print("φ (ºC)' = ",ang*180/math.pi)

print("\ng) Angulo adyacente límite φlim (mrad): ")
anglim = pow(5400/f,1/3)
print("φlim (mrad)' = ",anglim)

print("\nh) Condición: ")
if (ang*1000 > anglim):
    tipo = 1
    print("Reflexión por tierra curva"\n)
else:
    tipo2
    print("Difracción por tierra curva\n")

if(tipo == 1):
    er = float(input('Permitividad relativa εr: '))
    sigma = float(input('Conductividad del medio σ: '))
    ec = er - 60 * sigma * l * 1j
    Zh = numpy.sqrt(ec - pow(math.cos(ang), 2))
    Zv = numpy.sqrt(ec - pow(math.cos(ang), 2)) / ec
    if (pol == 1):
        #Polarizacion horizontal
        Rv = (math.sin(ang) - Zv) / (math.sin(ang) + Zv)
        (r, phi) = cmath.polar(-Rv)
        print("\ni) Coeficiente de reflexión Rv: ")
        print('Rv  = ', Rv)
        print('|Rv| = ', r, ', θ = ', phi * 180 / math.pi)
    elif (pol == 2):
        #Polarizacion vertical
        Rh = (math.sin(ang) - Zh) / (math.sin(ang) + Zh)
        (r, phi) = cmath.polar(-Rh)
        print("\ni) Coeficiente de reflexión Rh: ")
        print('Rh  = ', Rh)
        print('|Rh| = ', r, ', θ = ', phi * 180 / math.pi)

print("\nj) Coeficiente de divergencia D: ")
D = pow(1 + (5/(16*k))*d1*d1*d2/(d*htp),-1/2)
print('D = ', D)