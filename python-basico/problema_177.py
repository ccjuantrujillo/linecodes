cadena = raw_input('Escribe una frase: ')
filtrado = cadena.strip()
resultado = 0
if len(filtrado.split()) == 1:
    for var in range(0,len(filtrado.split()[0])):
        if filtrado.split()[0][var:var+1] == '1' or filtrado.split()[0][var:var+1] == '2' or filtrado.split()[0][var:var+1] == '3' or filtrado.split()[0][var:var+1] == '4' or filtrado.split()[0][var:var+1] == '5' or filtrado.split()[0][var:var+1] == '6' or filtrado.split()[0][var:var+1] == '7' or filtrado.split()[0][var:var+1] == '8' or filtrado.split()[0][var:var+1] == '9' or filtrado.split()[0][var:var+1] == '.' or filtrado.split()[0][var:var+1] == 'e' or filtrado.split()[0][var:var+1] == '+' or filtrado.split()[0][var:var+1] == '-' or filtrado.split()[0][var:var+1] == 'E':
            resultado = resultado + 1
    if resultado == 0:
        print 'Flotante Incorrecto'
    else:
        print 'Flotante Correcto'    

        