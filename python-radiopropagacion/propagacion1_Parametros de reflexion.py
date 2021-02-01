import cmath
import math
import numpy

print("Variables de reflexión d1(km), d2(km), dv(km) ht'(m), hr'(m), φ (mrad) y D")
print('========================================================================= ')
ht = float(input('Horizonte de la antena transmisora ht (m): '))
hr = float(input('Horizonte de la antena receptora hr (m): '))
d  = float(input('Distancia del enlace d (km): '))
k  = float(input('Constante k: '))
f  = float(input('Frecuencia (Mhz): '))
sigma = float(input('Rugosidad del terreno σc: '))

#Parametro p
p = (2/numpy.sqrt(3))*numpy.sqrt(6.37*k*(ht+hr) + pow(d/2,2))

#Parametro α
alpha = math.acos(12.74*k*(ht-hr)*d/pow(p,3))

#Parametro d1, d2, dv, ht', hr' y φ
Re  = 6370
d1  = (d/2) + p*math.cos((math.pi+alpha)/3)
d2  = d - d1
dv  = 3.57*(numpy.sqrt(k*ht) + numpy.sqrt(k*hr))
htp = ht - pow(d1,2)*1000/(2*k*Re)
hrp = hr - pow(d2,2)*1000/(2*k*Re)
ang = math.atan((htp + hrp)/(d*1000))#rad
anglim = pow(5400/f,1/3)#mrad
D  = pow(1 + (5/(16*k))*d1*d1*d2/(d*htp),-1/2)
dl = 2*htp*hrp/(d*1000)
dt = math.pi*f*dl/150

print('d1(km) = ',d1)
print('d2(km) = ',d2)
print('dv(km) = ',dv)
print("ht'(m) = ",htp)
print("hr'(m) = ",hrp)
print("Angulo de incidencia φ(mrad)' = ",ang*1000)
print("Angulo de incidencia φ(ºC)'   = ",ang*180/math.pi)
print("φlim(mrad)' = ",anglim)
print("φlim(ºC)'   = ",anglim*180/(math.pi*1000))
print('Coef. de divegencia D = ', D)
print('Dif. de trayectos ΔL(m) = ', dl)
print('Dif. de fase Δθ(rad) = ', dt)