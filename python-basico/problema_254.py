p = int(raw_input('Dime el numero de culumnas: '))
q = int(raw_input('Dime el numero de filas: '))

A=[]
for i in range(p):
    A.append([0]*q)

#print A

aux = p

if q <= p:
    aux = q

V = [0]*aux

print 'Lectura de la matriz A'
for i in range(p):
    for j in range(q):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

for k in range(aux):
    for i in range(k+1):
        for j in range(k+1):
            V[k]=V[k]+A[i][j]

print 'Resultado'

print V

