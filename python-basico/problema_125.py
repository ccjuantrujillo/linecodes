n = int(raw_input('Ingrese el primer numero: '))
m = int(raw_input('Ingrese el segundo numero: '))
suma = 0
for var in range(n,m+1,2):
    suma += var
print 'La suma de los pares entre los valores %d y %d es %d' %(n,m,suma)