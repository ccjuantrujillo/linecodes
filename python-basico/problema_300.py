def si_o_no(pregunta):
    resultado = ''
    while resultado != 'si' or resultado != 's' or resultado != 'Si' or resultado != 'SI' or resultado != 'no' or resultado != 'n' or resultado != 'No' or resultado != 'NO':  
        print pregunta
        resultado = str(raw_input('Escriba su respuesta: '))
        if resultado == 'si' or resultado == 's' or resultado == 'Si' or resultado == 'SI':
            salida = True
            break
        elif resultado == 'no' or resultado == 'n' or resultado == 'No' or resultado == 'NO':
            salida = False
            break
        else:
            print 'Solo puede elegir si o no'
    return salida

pregunta = 'Usted es mayor de edad'

print si_o_no(pregunta)
            
    
