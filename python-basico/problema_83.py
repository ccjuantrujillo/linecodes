a = int(raw_input('Dame el primer numero'))
b = int(raw_input('Dame el segundo numero'))
c = int(raw_input('Dame el tercer numero'))
d = int(raw_input('Dame el cuarto numero'))
e = int(raw_input('Dame el quinto numero'))

var_1 = b-a
var_2 = c-a
var_3 = d-a
var_4 = e-a

menor = var_1

if var_2 < menor:
    menor = var_2
if var_3 < menor:
    menor = var_3
if var_4 < menor:
    menor = var_4

valor = menor + a

print 'El numero que mas se aproxima de los cuatro al primero es:',valor



