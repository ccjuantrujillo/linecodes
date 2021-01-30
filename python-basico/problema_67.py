x = float(raw_input('Ingrese el interes: '))

if x > 0:
    capital = float(raw_input('Ingrese el capital: '))
    numero = float(raw_input('Ingrese la cantidad de años: '))
    valor = capital *( (1 + x/100)**numero)
    print 'El capital final es:',valor

