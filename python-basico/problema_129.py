n = int(raw_input('Ingrese el primer numero: '))
m = int(raw_input('Ingrese el segundo numero: '))
con = 1
var = 0
if n > m:
    while con <= m:
        if n % con == 0 and m % con == 0:
            var = con
        con += 1
else:
    while con <= n:
        if n % con == 0 and m % con == 0:
            var = con
        con += 1

print 'El MCD de %d y %d es %d' %(n,m,var)