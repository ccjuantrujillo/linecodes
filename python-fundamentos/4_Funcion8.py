#area y angulo
from math import sqrt,asin,pi

def area_triangulo(a,b,c):
    s = (a+b+c)/2.0
    return sqrt(s*(s-a)*(s-b)*(s-c))

#print area_triangulo(3,4,5)

def angulo_alfa(a,b,c):
    s = area_triangulo(a,b,c)
    return 180 / pi * asin(2.0*s/b*c)

def menu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print '1) Calcular el area del triangulo'
        print '2) Calcular angulo opuesto al primer lado'
        opcion = int(raw_input('Escoge opcion: '))
    return opcion

lado1 = float(raw_input('Dame lado a: '))
lado2 = float(raw_input('Dame lado b: '))
lado3 = float(raw_input('Dame lado c: '))

s = menu()

if s == 1:
    resultado = area_triangulo(lado1,lado2,lado3)
else:
    resultado = angulo_alfa(lado1,lado2,lado3)

print 'Escogiste la opcion:',s
print 'El resultado es',resultado

    