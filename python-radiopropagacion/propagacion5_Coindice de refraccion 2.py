#Calcula el coíndice de refracción Ns en función de No y hs
import math

#Ingresamos datos
No = float(input('Ingrese el coíndice de refracción No: '))
hs = float(input('Ingrese la altura hs(Km): '))

#Cálculos
Re = 6370
Ns = No*math.exp(-0.136*hs)
G  = (Ns - No)/(hs*1000)
R  = -1e+6/(G*1000)
k  = 1/(1-Re/R)
Gm = G + 1e+6/Re
Req = k*Re

#Resultados
print('\nCoíndice de refracción a una altura  Ns = ',Ns)
print('Gradiente ΔN/Δh(m) = ', G)
print('Gradiente ΔM/Δh(m)= ',Gm)
print('Indice de refracción k = ',k)
print('Radio de trayectoria R(km) = ',R)
print('Radio de la tierra Re(km) = ',Re)
print('Radio equivalente Req(km) = ',Req)