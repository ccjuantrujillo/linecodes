cantidad = int(raw_input('Ingrese la cantidad: '))

num_500 = int(cantidad / 500)

aux_1 = int(cantidad - (500 * num_500 ))

num_200 = 0
num_100 = 0
num_50 = 0
num_20 = 0
num_10 = 0
num_5 = 0
num_2 = 0
num_1 = 0

if aux_1 > 0:
    num_200 = int( aux_1 / 200 )

aux_2 = int(aux_1 - (200 * num_200 ))

if aux_2 > 0:
    num_100 = int( aux_2 / 100 )

aux_3 = int(aux_2 - (100 * num_100 ))

if aux_3 > 0:
    num_50 = int( aux_3 / 50 )

aux_4 = int(aux_3 - (50 * num_50 ))

if aux_4 > 0:
    num_20 = int( aux_4 / 20 )

aux_5 = int(aux_4 - (20 * num_20 ))

if aux_5 > 0:
    num_10 = int( aux_5 / 10 )

aux_6 = int(aux_5 - (10 * num_10 ))

if aux_6 > 0:
    num_5 = int( aux_6 / 5 )

aux_7 = int(aux_6 - (5 * num_5 ))

if aux_7 > 0:
    num_2 = int( aux_7 / 2 )

num_1 = int(aux_7 - (2 * num_2 ))

if num_1 > 0:
    num_1 = num_1        

print num_500,'Billetes de 500'
print num_200,'Billetes de 200'
print num_100,'Billetes de 100'
print num_50,'Billetes de 50'
print num_20,'Billetes de 20'
print num_10,'Billetes de 10'
print num_5,'Billetes de 5'
print num_2,'Billetes de 2'
print num_1,'Billetes de 1'