cadena = raw_input('Escribe una frase: ')

#elimina los espacios en blanco a la izquierda y a la derecha
filtrado = cadena.strip()

resultado = 0

for var in range(0,len(filtrado)):
    if filtrado[var:var+1] == '1' or filtrado[var:var+1] == '0':
        resultado = resultado + 1
        

if resultado == len(filtrado):
    print 'SI es un numero binario'
else:
    print 'NO es un numero binario'