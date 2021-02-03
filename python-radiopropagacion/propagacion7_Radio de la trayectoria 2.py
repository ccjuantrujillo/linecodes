#Calcula del radio de la trayectoria "R" en función de k

k = float(input('Ingrese el valor de k: '))

Re  = 6370
R   = Re/(1-1/k)
k   = 1/(1-Re/R)
G   = -1e+6/(R*1000)
Gm  = G + 1e+6/Re
Req = k*Re

print('Radio de trayectoria R(km) = ',R)
print('Gradiente ΔN/Δh(m) = ',G)
print('Gradiente ΔM/Δh= ',Gm)
print('Radio equivalente Req(km) = ',Req)