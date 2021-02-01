import math

print('1) Calculo del coíndice de refracción a una altura (Ns): ')
P = float(input('Presión atmosférica P(hPa): '))
H = float(input('Humedad relativa H(%): '))
t = float(input('Temperatura T(ºC): '))
hs = float(input('Ingrese la altura hs(Km): '))
p = int(input('Seleccione para el agua (1) o hielo (2): '))

print('\na) Obtenemos la presión del vapor de agua (hPa): ')
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
print('e = ',e)

print('\nb) Obtenemos el coíndice de refracción a nivel del mar (No): ')
No = (77.6/T)*(P + 4810*e/T)
print('No = ',No)

print('\nc) Obtenemos el coíndice de refracción a una altura (Ns): ')
Ns = No*math.exp(-0.136*hs)
print('Ns = ',Ns)

if hs != 0:
    Re  = 6370
    print('\nd) Indice de refracción modificado M: ')
    M 0 n + (hs/Re)*1e+6
    print('M = ', M)
    print('\ne) Radio de la trayectoria R(km): ')
    R = -1e+6*hs/(Ns - No)
    print('R(km) = ', R)
    print('\nf) Indice de refracción k: ')
    k = 1/(1-Re/R)
    print('k = ', k)
