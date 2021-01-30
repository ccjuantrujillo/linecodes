numero = float(raw_input('Ingrese el numero: '))

for var in range(2,101):
    print 'la raiz %d-enesima de %f es %f' % (var,numero,numero**(1.0/var))
