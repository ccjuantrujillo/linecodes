a = int(raw_input('Dame el primer numero'))
b = int(raw_input('Dame el segundo numero'))
c = int(raw_input('Dame el tercer numero'))
d = int(raw_input('Dame el cuarto numero'))
e = int(raw_input('Dame el quinto numero'))

candidato_1 = a

if b > candidato_1:
    candidato_1 = b
if c > candidato_1:
    candidato_1 = c 

candidato_2 = candidato_1

if d > candidato_2:
    candidato_2 = d
if e > candidato_2:
    candidato_2 = e

print 'El mayor valor de los tres es',candidato_2

    

    
    
    
