def estudiantes_aprobados(alumnos,notas):
    for i in range(len(alumnos)):
        if notas[i] > 10:
            print 'El alumno ' + str(alumnos[i]) + ' ha aprobado el examen con nota: ' + str(notas[i]) + '. '

def numero_de_aprobados(alumnos,notas):
    contador = 0
    for i in range(len(alumnos)):
        if notas[i] > 10:
            contador +=1

    return contador

def estudiantes_con_maxima_nota(alumnos,notas):
    maxima = max(notas)
    for i in range(len(alumnos)):
        if notas[i] == maxima:
            print 'El alumno ' + str(alumnos[i]) + ' obtuvo la nota maxima' + str(maxima) + '. '

def nota_promedio(notas):
    suma = 0
    for  i in range(len(notas)):
        suma  = suma + notas[i]
    return suma/len(notas)



def estudiantes_con_mayor_a_la_media(alumnos,notas):
    promedio = nota_promedio(notas)
    for  i in range(len(notas)):
        if notas[i] >= promedio:
            print 'El alumno ' + str(alumnos[i]) + ' obtuvo nota mayor que la media' + str(promedio) + '. '

def muestra_nota_de_alumno(alumnos,notas,alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            return notas[i]
            break


alumnos = ['Alexander','Edward','Karin','Betsy']
notas = [20,18,16,19]

estudiantes_aprobados(alumnos,notas)

print numero_de_aprobados(alumnos,notas)

estudiantes_con_maxima_nota(alumnos,notas)

estudiantes_con_mayor_a_la_media(alumnos,notas)

alumno_buscado = 'Edward'

print muestra_nota_de_alumno(alumnos,notas,alumno_buscado)

