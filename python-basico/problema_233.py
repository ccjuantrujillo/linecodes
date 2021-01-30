a = [1,2,1,5,0,3,4,5,2,5,4,4,5,5,5,2]

numero = len(a)

var = numero % 2

if var == 0:
    limite = numero/2
else:
    limite = (numero+1)/2

print limite

i = 0

while i < limite:
    del a[i]
    i = i + 1

print a