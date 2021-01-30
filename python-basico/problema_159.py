cadena = str(raw_input('Ingrese la cadena: '))
con = 0
for i in range(len(cadena)):
    if cadena[i] == ' ':
        con = con + 1
print 'La cadena tiene esta cantidad',con,'de espacios vacios'