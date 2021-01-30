#matrices
m = int(raw_input('Dame el numero de filas: '))
n = int(raw_input('Dame el numero de columnas: '))

M = []

for i in range(m):
    M.append([0]*n)

print M

for j in range(m):
    for k in range(n):
        M[j][k] = int(raw_input('Dame el componente (%d,%d): ' % (j,k) ))

print M

