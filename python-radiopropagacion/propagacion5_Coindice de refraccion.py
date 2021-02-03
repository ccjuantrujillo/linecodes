#Calcula el coíndice de refracción Ns a una altura hs según P, H, t, hs y p
import math

#Ingresamos datos
P = float(input('Presión atmosférica P(hPa): '))
H = float(input('Humedad relativa H(%): '))
t = float(input('Temperatura T(ºC): '))
hs = float(input('Ingrese la altura hs(Km): '))
p = int(input('Seleccione para el agua (1) o hielo (2): '))

#Calculos
if p == 1: #para el agua
    a = 6.1121
    b = 17.502
    c = 240.97
elif p == 2: #para el hielo
    a = 6.1115
    b = 22.452
    c = 272.55
T = t + 273
es = a*math.exp(b*t/(t+c))
e  = H * es / 100
No = (77.6/T)*(P + 4810*e/T)
Ns = No*math.exp(-0.136*hs)
if hs != 0:
    Re  = 6370
    M = No + (hs/Re)*1e+6
    R = -1e+6*hs/(Ns - No)
    k = 1/(1-Re/R)
    G = (Ns - No)/(hs*1000)

#Mostramos resultados
print('\nPresión del vapor de agua e(hPa) = ',e)
print('Coíndice de refracción a nivel del mar No = ',No)
print('Coíndice de refracción a una altura  Ns = ',Ns)
if hs != 0:
    print('Indice de refracción modificado M = ', M)
    print('Radio de la trayectoria R(km) = ', R)
    print('Indice de refracción k = ', k)
    print('Gradiente G (ΔN/Δh) /m = ', G)