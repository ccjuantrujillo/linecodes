p = int(raw_input('Dime el numero de filas: '))
q = int(raw_input('Dime el numero de columnas: '))

A=[]
for i in range(p):
    A.append([0]*q)

C=[0]*p

print 'Lectura de la matriz A'
for i in range(p):
    for j in range(q):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))


for i in range(p):
    for j in range(q):
        C[i]=C[i]+A[i][j]

print 'Resultado'
print C