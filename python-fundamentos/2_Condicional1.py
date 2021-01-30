#Compra de llantas con descuento
#Extraidos del libro
#http://blog.espol.edu.ec/icm00794/files/2017/05/PYTHON_PROGRAMACION_V3_0.pdf
n=int(input('Cantidad de llantas: '))
p=float(input('Precio unitario: '))
if(n>4):
    p=0.9*p
t = n*p
print('Valor a pagar: ',t)