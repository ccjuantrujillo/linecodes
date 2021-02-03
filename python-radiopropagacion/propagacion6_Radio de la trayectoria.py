#Calcula del radio de la trayectoria "R" en función de la gradiente G (ΔN/Δh) /m

G = float(input('Ingrese el gradiente G (ΔN/Δh) /m: '))

Re = 6370
R  = -1e+6/G
k  = 1/(1-Re/R)
Gm = G + 1e+6/Re
Req = k*Re

print('\nRadio de trayectoria R(km) = ',R)
print('Indice de refracción k = ',k)
print('Radio de la tierra Re(km) = ',Re)
print('Radio equivalente Req(km) = ',Req)
print('Gradiente ΔM/Δh(m)= ',Gm)
