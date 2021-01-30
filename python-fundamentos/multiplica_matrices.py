#pedimos la dimension de las matrices
p = int(raw_input('Dime el numero de filas da A: '))
q = int(raw_input('Dime el numero de columnas de A (y filas de B): '))
r = int(raw_input('Dime el numero de columnas B: '))

#creamos dos matrices nulas
A=[]
for i in range(p):
    A.append([0]*q)

B=[]
for i in range(q):
    B.append([0]*r)


#y leeemos sus contenidos por teclado
print 'Lectura de la matriz A'
for i in range(p):
    for j in range(q):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

print 'Lectura de la matriz B'
for i in range(q):
    for j in range(r):
        B[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

C= []
for i in range(p):
    C.append([0]*r)

#empieza el calculo de la multiplicacion
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j]= C[i][j] + A[i][k]*B[k][j]
        

#y mostramos el resultado por pantalla
print 'Multiplica'
for i in range(p):
    for j in range(r):
        print C[i][j]
    print 






