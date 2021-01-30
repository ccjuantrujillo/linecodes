#Calculo del pago semanal
#Extraidos del libro
#http://blog.espol.edu.ec/icm00794/files/2017/05/PYTHON_PROGRAMACION_V3_0.pdf
c=float(input('Horas trabajadas: '))
t=float(input('Tarifa por hora: '))
d=float(input('Descuento: '))
if c<=40:
    p=c*t - d
else:
    p=40*t + 1.5*t*(c-40) - d
print('Valor a pagar',p)