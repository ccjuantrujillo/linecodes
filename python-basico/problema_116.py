from math import *

print '1) Introducir el primer vector: '
x_1 = float(raw_input('Ingrese x: '))
y_1 = float(raw_input('Ingrese y: '))
z_1 = float(raw_input('Ingrese z: '))
    
    

print '2) Introducir el segundo vector: '
x_2 = float(raw_input('Ingrese x: '))
y_2 = float(raw_input('Ingrese y: '))
z_2 = float(raw_input('Ingrese z: '))

opcion_2 = 1

while opcion_2 != 9:
    
    print '3) Calcular la suma. '
    print '4) Calcular la diferencia. '
    print '5) Calcular el producto escalar. '
    print '6) Calcular el producto vectorial. '
    print '7) Calcular el angulo (en grados) entre ellos. '
    print '8) Calcular la longitud. '
    print '9) Finalizar. '
    
    opcion_2 = int(raw_input('Teclea un numero y pulsa el retorno de carro: '))

    if opcion_2 == 3 :
        x_3 = x_1 + x_2
        y_3 = y_1 + y_2
        z_3 = z_1 + z_2
        print 'El vector suma es: ',x_3,y_3,z_3

    if opcion_2 == 4 :
        x_3 = x_1 - x_2
        y_3 = y_1 - y_2
        z_3 = z_1 - z_2
        print 'El vector diferencia es: ',x_3,y_3,z_3

    if opcion_2 == 5 :
        producto_escalar = x_1*y_1 + x_2*y_2 + x_3*y_3
        print 'El productos escalar de los dos vectores es:',producto_escalar        

    if opcion_2 == 6 :
        x_3 = y_1*z_2 - z_1*y_2
        y_3 = z_1*x_2 - x_1*z_2
        z_3 = x_1*y_2 - y_1*x_2
        print 'El producto vectorial de los dos vectores es:',x_3,y_3,z_3

    if opcion_2 == 7 :
        var_1 = float(x_1*y_1 + y_2*y_2 + z_1*z_2)
        var_2 = float((x_1**2 + y_1**2 + z_1**2)**0.5)
        var_3 = float((x_2**2 + y_2**2 + z_2**2)**0.5)
        angulo = float((180/3.1416)*(acos(float(var_1/(var_2*var_3)))))
        print 'El angulo entre los dos vectores es:',angulo         

    if opcion_2 == 8 :
        l_1 = (x_1**2 + y_1**2 + z_1**2)**0.5
        l_2 = (x_2**2 + y_2**2 + z_2**2)**0.5       
        print 'La longitud de los vectorees es:',l_1,l_2 


print 'Gracias por usar este programa'           