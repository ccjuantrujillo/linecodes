num = 3
mayor = 0
while num > 0:
    num = int(raw_input('Ingrese un numero: '))
    if num > mayor:
        mayor = num
print 'El mayor numero ingresado es: ',mayor