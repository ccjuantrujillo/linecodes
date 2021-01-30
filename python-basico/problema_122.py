numero = int(raw_input('Ingrese un numero: '))
print '1) Ordenar de forma ascendente.'
print '2) Ordenar de forma ascendente.'
opcion = int(raw_input('Ingrese la opcion: '))
var=0
if opcion == 1:
    for var in range(2,numero+1,2):
        print var

if opcion == 2:
    for var in range(numero,1,-2):
        print var