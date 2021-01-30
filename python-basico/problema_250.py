#pedimos la dimension de las matrices
m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))

#creamos dos matrices nulas
A=[]
for i in range(m):
    A.append([0]*n)

B=[]
for i in range(m):
    B.append([0]*n)


#y leeemos sus contenidos por teclado
print 'Lectura de la matriz A'
for i in range(m):
    for j in range(n):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

print 'Lectura de la matriz A'
for i in range(m):
    for j in range(n):
        B[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

C= []
for i in range(m):
    C.append([0]*n)

#empieza el calculo de la suma
for i in range(m):
    for j in range(n):
        C[i][j]=A[i][j]-B[i][j]

#y mostramos el resultado por pantalla
print 'Suma'
for i in range(m):
    for j in range(n):
        print C[i][j]
    print 






