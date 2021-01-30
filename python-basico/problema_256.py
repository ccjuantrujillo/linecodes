n = int(raw_input('Ingrese la dimension de la matriz: '))

A=[]

for i in range(n):
    A.append([0]*n)

for i in range(n):
    for j in range(n):
        A[i][j]= float(raw_input('Dame el componente (%d , %d) '% (i,j)))

aux = 0

for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            aux = aux + 1
var = n*(n+1)/2

if aux == var:
    print 'La matriz es diagonal superior'
else:
    print 'La matriz no es diagonal superior'    
