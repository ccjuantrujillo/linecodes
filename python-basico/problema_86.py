from math import log

capital_final = float(raw_input('Ingrese el capital final: '))

capital_inicial = float(raw_input('Ingrese el capital inicial: '))

tasa_anual = float(raw_input('Ingrese la tasa anual: '))

if tasa_anual < 0:
    print 'Debe ingresar una tasa anual positiva'
else:
    if capital_final == capital_inicial:
        print 'El capital inicial y final deben ser distintos'
    else:
        n = (log(capital_final)-log(capital_inicial))/(log(1+tasa_anual/100))
        print 'La cantidad de tiempo que debe dejar su capital es de:',n
    