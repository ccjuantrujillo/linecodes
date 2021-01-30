cadena = raw_input('Escribe una frase: ')

#elimina los espacios en blanco a la izquierda y a la derecha
filtrado = cadena.strip()

contador = 0 
valor = 0

for var in range(0,len(filtrado)):
    if filtrado[var:var+1] == '1' or filtrado[var:var+1] == '0':
        contador = contador + 1

if contador == len(filtrado):
    for bit in cadena:
        valor += valor + int(bit)
    print 'Su valor decimal es:',valor
else:
    print 'Numero binario mal formado'    
