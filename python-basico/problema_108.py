n = int(raw_input('Ingrese el primer numero: '))

m = int(raw_input('Ingrese el segundo numero: '))

if n > m:
    print 'No se efectuaran ningun calculo'
else:
    sumatoria = 0
    i = n
    while i <= m:
        sumatoria += i
        i+=1
    print sumatoria

