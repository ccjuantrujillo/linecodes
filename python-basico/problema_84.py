from math import sqrt

punto_x_1 = float(raw_input('Ingrese la abcisa del primer punto: '))
punto_y_1 = float(raw_input('Ingrese la ordenada del primer punto: '))

punto_x_2 = float(raw_input('Ingrese la abcisa del segundo punto: '))
punto_y_2 = float(raw_input('Ingrese la ordenada del segundo punto: '))

punto_x_3 = float(raw_input('Ingrese la abcisa del tercer punto: '))
punto_y_3 = float(raw_input('Ingrese la ordenada del tercer punto: '))

punto_x_4 = float(raw_input('Ingrese la abcisa del cuarto punto: '))
punto_y_4 = float(raw_input('Ingrese la ordenada del cuarto punto: '))

punto_x_5 = float(raw_input('Ingrese la abcisa del quinto punto: '))
punto_y_5 = float(raw_input('Ingrese la ordenada del quinto punto: '))

d_1 = sqrt((punto_x_2-punto_x_1)**2 + (punto_y_2-punto_y_1)**2)
d_2 = sqrt((punto_x_3-punto_x_1)**2 + (punto_y_3-punto_y_1)**2)
d_3 = sqrt((punto_x_4-punto_x_1)**2 + (punto_y_4-punto_y_1)**2)
d_4 = sqrt((punto_x_5-punto_x_1)**2 + (punto_y_5-punto_y_1)**2)

menor = d_1

if d_2 < menor:
    menor = d_2
if d_3 < menor:
    menor = d_3
if d_4 < menor:
    menor = d_4

if menor == d_1:
    print 'El segundo punto es el mas cercano al primero'
if menor == d_2:
    print 'El tercer punto es el mas cercano al primero'
if menor == d_3:
    print 'El cuarto punto es el mas cercano al primero'
if menor == d_4:
    print 'El quinto punto es el mas cercano al primero'


    