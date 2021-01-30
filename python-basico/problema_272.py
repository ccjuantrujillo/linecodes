#cadena[0:1]

def es_repeticion(cadena):
    var = len(cadena)

cadena = 'Alexander'

E=[]
for i in range (len(cadena)+1):
    E.append(cadena[0:i])

print E[6]
print cadena
print cadena[0:2]
print cadena[2:4]
print cadena[4:6]
print cadena[6:8]
print '---------'
print len(cadena)
print '---------'
if len(cadena)%2 == 0:
    contador = int(len(cadena) / 2)
else:
    contador = int((len(cadena)-1)/2)

print contador

for i in range(contador+1):
    print E[i]
    
