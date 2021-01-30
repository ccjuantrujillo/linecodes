cadena = raw_input('Introduce una cadena: ')

print len(cadena)

print cadena[len(cadena)-1:len(cadena)]
print cadena[len(cadena)-2:len(cadena)-1]
print cadena[len(cadena)-3:len(cadena)-2]

resultado = cadena[len(cadena)-3:len(cadena)-2]  + cadena[len(cadena)-2:len(cadena)-1] + cadena[len(cadena)-1:len(cadena)]

print resultado

for var in range(0,len(cadena)):
    if cadena[var:var+1] =='.':
        valor = var
        break
        
final = len(cadena) - (valor +1)

print len(cadena)
print valor
print final

valor_final = ''

for indicador in range(len(cadena),valor+1,-1):
    valor_final = cadena[indicador-1:indicador] + valor_final

print 'La extension del archivo es:',valor_final