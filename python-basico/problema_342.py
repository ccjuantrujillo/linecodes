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
            print 'El alumno: ' + str(alumnos[i]) + ' obtuvo la nota maxima: ' + str(maxima)

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

def nuevo_alumno_calificacion(alumnos,notas):
    var_1 = str(raw_input('Ingrese el nombre del nuevo alumno: '))
    var_2 = int(raw_input('Ingrese la calificacion del nuevo alumno: '))
    alumnos.append(var_1)
    notas.append(var_2)

def todos_los_alumnos(alumnos,notas):
    for i in range(len(alumnos)):
        print 'Alumno: ' + str(alumnos[i]) + ' calificacion: ' + str(notas[i])


alumnos = ['Alexander','Edward','Karin','Betsy']
notas = [20,18,16,19]

#estudiantes_aprobados(alumnos,notas)

#print numero_de_aprobados(alumnos,notas)

#estudiantes_con_maxima_nota(alumnos,notas)

#estudiantes_con_mayor_a_la_media(alumnos,notas)

#alumno_buscado = 'Edward'

#print muestra_nota_de_alumno(alumnos,notas,alumno_buscado)

print 'Menu de aplicacion del sistema de alumnos y notas'
print '================================================='
print '[1] Anadir estudiante y calificacion'
print '[2] Mostrar lista de estudiantes con sus calificaciones'
print '[3] Calcular la media de las calificaciones'
print '[4] Calcular el numero de aprobados'
print '[5] Mostrar los estudiantes con mejor calificacion'
print '[6] Mostrar los estudiantes con calificacion superior a la media'
print '[7] Consultar la nota de un estudiante determinado'
print '[8] FINALIZAR EJECUCION DEL PROGRAMA'
opcion = int(raw_input('Escoja su opcion: '))

if opcion == 1:
    nuevo_alumno_calificacion(alumnos,notas)

if opcion == 2:
    todos_los_alumnos(alumnos,notas)

if opcion == 3:
    aux = nota_promedio(notas)
    print 'La nota promedio del salon es:',aux

if opcion == 4:
    aux = numero_de_aprobados(alumnos,notas)
    print 'La cantidad de alumnos aprobados es:',aux

if opcion == 5:
    print 'Los alumnos que obtuvieron la maxima calificacion son:'
    estudiantes_con_maxima_nota(alumnos,notas)

if opcion == 6:
    print 'Los alumnos que obtuvieorn nota mayor a la media son: '
    estudiantes_con_mayor_a_la_media(alumnos,notas)

if opcion == 7:
    aux = str(raw_input('Ingrese el nombre del alumno a buscar: '))
    nota = muestra_nota_de_alumno(alumnos,notas,aux)
    print 'La nota del alumno: '+ aux + ' es: ' + str(nota)

    






