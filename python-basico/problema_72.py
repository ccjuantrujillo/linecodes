valor = str(raw_input('Ingrese un caracter: '))

if  valor >= 'a'  and valor <= 'z':
    print 'MINUSCULA'
else:
    if valor >= 'A'  and valor <= 'Z':
        print 'MAYUSCULA'
    else:
        numero = ord(valor)
        if numero == 164 or numero == 165:
            print 'Usted ingreso una',chr(164),'o',chr(165)
        else:
            print 'No es una letra'

    