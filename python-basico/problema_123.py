n = int(input('Ingrese el primer numero: '))
m = int(input('Ingrese el segundo numero: '))
suma = 0
for var in range(n,m+1):
    suma += var
print('La suma entre los valores %d y %d es %d' %(n,m,suma))
