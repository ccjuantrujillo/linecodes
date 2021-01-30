lista = []

numero = int(raw_input('Dame un numero'))


for var in range(0,10):
    numero = int(raw_input('Dame un numero'))
    if numero < 0:
        print 'Ingrese un numero positivo'
        numero = int(raw_input('Dame un numero'))
    else:
        lista.append(numero)
        
    