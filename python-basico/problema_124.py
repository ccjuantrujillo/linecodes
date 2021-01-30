n = int(raw_input('Ingrese el primer numero: '))
m = int(raw_input('Ingrese el segundo numero: '))
suma = 0
for var in range(n,m+1):
    suma += var**2
print 'La suma de los ciuadrados entre los valores %d y %d es %d' %(n,m,suma)