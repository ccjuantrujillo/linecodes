#ord('a')=97
#chr(97)= a
#chr(ord('a')+3)= d

cadena = str(raw_input('Ingrese una cadena: '))

numero = int(raw_input('Ingrese un numero entero '))

resultado = ''

auxiliar_1 = ''
auxiliar_2 = 0
auxiliar_3 = ''
auxiliar_4 = ''

for variable in range(0,len(cadena.split())):
    for var in range(0,len(cadena.split()[variable])):
        if cadena.split()[variable][var:var+1] == '1' or cadena.split()[variable][var:var+1] == '2' or cadena.split()[variable][var:var+1] == '3' or cadena.split()[variable][var:var+1] == '4' or cadena.split()[variable][var:var+1] == '5' or cadena.split()[variable][var:var+1] == '6' or cadena.split()[variable][var:var+1] == '7' or cadena.split()[variable][var:var+1] == '8' or cadena.split()[variable][var:var+1] == '9':
            auxiliar_5 = int(cadena.split()[variable][var:var+1])
            auxiliar_6 = auxiliar_5 - numero
            resultado = resultado + str(auxiliar_6)
        else:
            auxiliar_1 = cadena.split()[variable][var:var+1]
            auxiliar_2 = ord(auxiliar_1)
            auxiliar_3 = auxiliar_2 - numero
            auxiliar_4 = chr(auxiliar_3)
            resultado = resultado + auxiliar_4
    resultado = resultado + ' '

print resultado
    