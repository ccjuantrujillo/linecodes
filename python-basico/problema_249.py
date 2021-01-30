n = int(raw_input('Ingrese un numero: '))

M = []

for i in range(n):
    M.append([0]*n)

print M

for j in range(n):
    M[j][j] = 1

print M