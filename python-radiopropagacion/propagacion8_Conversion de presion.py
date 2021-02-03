#Convierte la presión de hPa o mBar a otras unidades

#Ingresamos datos
P = float(input('Presión atmosférica P(hPa) o P(mBar): '))

#Calculos
Pa = P/1013.25
Ph = Pa*760

#Mostramos resultados
print('Presión P(atm) = ', Pa)
print('Presión P(mmHg) = ', Ph)