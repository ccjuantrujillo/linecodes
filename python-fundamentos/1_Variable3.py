#Programa para calcular el area de un triangulo
#Extraidos del libro
#http://blog.espol.edu.ec/icm00794/files/2017/05/PYTHON_PROGRAMACION_V3_0.pdf
from math import sqrt
a = float(input('Primer lado: '))
b = float(input('Segundo lado: '))
c = float(input('Tercer lado: '))
t = (a+b+c)/2
s = sqrt(t*(t-a)*(t-b)*(t-c))
print('Respuesta: ',s)