n = int(raw_input('Ingrese el primer numero: '))
m = int(raw_input('Ingrese el segundo numero: '))
p = int(raw_input('Ingrese el tercer numero: '))

menor = n

if m < menor:
    menor = m
if p < menor:
    menor = p

con = 1
var = 0

while con <= menor:
    if n % con == 0 and m % con == 0 and p % con == 0:
        var = con
    con += 1

print 'El MCD de %d , %d y %d es %d' %(n,m,p,var)