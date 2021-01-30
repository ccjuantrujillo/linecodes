lado_1 = float(raw_input('Ingrese el primer lado del triangulo: '))

lado_2 = float(raw_input('Ingrese el segundo lado del triangulo: '))

lado_3 = float(raw_input('Ingrese el tercer lado del triangulo: '))
 
semi_perimetro = (lado_1 + lado_2 + lado_3)*0.5

area = (semi_perimetro * (semi_perimetro - lado_1) * (semi_perimetro - lado_2) * (semi_perimetro - lado_3) )**0.5

print area