cadena = str(raw_input('Ingrese la cadena: '))
con = 0
for i in range(len(cadena)):
    if cadena[i] >= '0' and cadena[i] <= '9':
        con = con + 1
if con == 0:
    print 'No Contiene digito'
else:
    print 'Contiene digito'