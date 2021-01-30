numero = int(raw_input('Ingrese el numero: '))

a = numero % 2
b = numero/2
c = b % 2

if a == 0:    
    if c != 0:
        print 'El numero es el doble de un numero impar'
    if c == 0:
        print 'El numero no es el doble de un numero impar'        
if a != 0:
    print 'El numero no es el doble de un numero impar'        
    
    
 

