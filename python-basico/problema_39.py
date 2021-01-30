capital = float(raw_input('Ingrese el capital: '))

interes = float(raw_input('Ingrese el interes: '))

tiempo = float(raw_input('Ingrese el tiempo: '))

capital_nuevo = capital * ( 1 + interes / 100 )** tiempo

print 'Nuevo capital',capital_nuevo