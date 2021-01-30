#pedimos la dimension de las matrices
m = int(raw_input('Dime el numero de filas: '))
n = int(raw_input('Dime el numero de columnas: '))
print '-----'
p = int(raw_input('Dime el numero a multiplicar: '))


#creamos dos matrices nulas
A=[]
for i in range(m):
    A.append([0]*n)

#y leeemos sus contenidos por teclado
print 'Lectura de la matriz A'
for i in range(m):
    for j in range(n):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

#multiplicamos la matriz por el numero leido
for i in range(m):
    for j in range(n):
        A[i][j]=A[i][j]*p

print 'Resultado'
for i in range(m):
    for j in range(n):
        print A[i][j]
    print 