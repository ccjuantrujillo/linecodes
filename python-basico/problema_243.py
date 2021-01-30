cadena = str(raw_input('Ingrese una cadena: '))

salida_1 = cadena.strip()

salida_2 = salida_1.split()

print salida_2
print len(salida_2)

resultado = ''

for i in range(0,len(salida_2)):
    resultado = resultado+ ' ' + salida_2[i]

resultado = resultado.strip()

print resultado
