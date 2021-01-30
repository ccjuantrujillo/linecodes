cadena = 'Edward'
Lista = []
for i in cadena:
    Lista.append(ord(i))

minimo = min(Lista)
maximo = max(Lista)

print 'Primera palabra: ' + str(chr(minimo))
print 'Ultima palabra: ' + str(chr(maximo))

