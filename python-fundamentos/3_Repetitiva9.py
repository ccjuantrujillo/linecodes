#es primo
num = int(raw_input('Dame un numero: '))

creo_que_es_primo = True
var = int(num**0.5)

for divisor in range(2,var):
    if num%divisor == 0:
        creo_que_es_primo = False
        break
    
    
if creo_que_es_primo:
    print 'El numero',num,'es primo'
else:
    print 'El numero',num,'no es primo'    

