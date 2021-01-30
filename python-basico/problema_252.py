m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))

A=[]
for i in range(n):
    A.append([0]*m)

B=[]
for i in range(m):
    B.append([0]*n)

print 'Lectura de la matriz A'
for i in range(n):
    for j in range(m):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))


for i in range(n):
    for j in range(m):
        B[j][i]=A[i][j]


print 'Resultado'
for i in range(m):
    for j in range(n):
        print B[i][j]

print A
print '--------------------------------'
print B
