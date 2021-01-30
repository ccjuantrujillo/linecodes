p = int(raw_input('Dime el numero de culumnas: '))
q = int(raw_input('Dime el numero de filas: '))

A=[]
for i in range(p):
    A.append([0]*q)

#print A
B=[0]*p
C=[0]*q
print 'Lectura de la matriz A'
for i in range(p):
    for j in range(q):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

for i in range(p):
    for j in range(q):
        B[i]= B[i] + A[i][j]

for i in range(q):
    for j in range(p):
        C[i]= C[i] + A[j][i]

print B
print '-----'
print C
