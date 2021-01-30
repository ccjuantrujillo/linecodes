##A = []
##A.append(4)
##A.append(6)
##print A
##print min(A)
##print max(A)

ciclistas = ['Pere Porcar','Joan Beltran','Lledo Fabra']

# 56852.8 58985.5 53963.8

tiempo = [[10092.0,12473.1,13723.3,10232.1,10332.3],[11726.2,11161.2,12272.1,11292.0,12534.0],[10193.4,10292.1,11712.9,10133.4,11632.0]]

def funcion_1(ciclistas,tiempo):
    suma=0
    Final = []
    for i in range(3):
        for j in range(5):
            suma = suma + tiempo[i][j]
        Final.append(suma)
        suma=0

    minimo = min(Final)
    
    for i in range(3):
        if Final[i] == minimo:
            resultado = ciclistas[i]
            break

    return resultado

print funcion_1(ciclistas,tiempo)

def funcion_2(ciclistas,tiempo,etapa):
    var = etapa -1
    Final = []
    for j in range(3):
        Final.append(tiempo[j][var])

    minimo = min(Final)

    for i in range(3):
        if Final[i] == minimo:
            resultado = ciclistas[i]
            break

    return resultado

#ciclistas = ['Pere Porcar','Joan Beltran','Lledo Fabra']
# 

print funcion_2(ciclistas,tiempo,1)

def funcion_3(ciclistas,tiempo):
    Final_1 = []
    Final_2 = []
    Final_3 = []
    Final_4 = []
    Final_5 = []
    
    for j in range(3):
        Final_1.append(tiempo[j][0])

    for j in range(3):
        Final_2.append(tiempo[j][1])

    for j in range(3):
        Final_3.append(tiempo[j][2])

    for j in range(3):
        Final_4.append(tiempo[j][3])

    for j in range(3):
        Final_5.append(tiempo[j][4])

    minimo_1 = min(Final_1)
    minimo_2 = min(Final_2)
    minimo_3 = min(Final_3)
    minimo_4 = min(Final_4)
    minimo_5 = min(Final_5)

    for i in range(3):
        if Final_1[i] == minimo_1:
            print 'El ganador de la Primera carrera es: ' + str(ciclistas[i])
            break

    for i in range(3):
        if Final_2[i] == minimo_2:
            print 'El ganador de la Segunda carrera es: ' + str(ciclistas[i])
            break

    for i in range(3):
        if Final_3[i] == minimo_3:
            print 'El ganador de la Tercera carrera es: ' + str(ciclistas[i])
            break

    for i in range(3):
        if Final_4[i] == minimo_4:
            print 'El ganador de la Cuarta carrera es: ' + str(ciclistas[i])
            break

    for i in range(3):
        if Final_5[i] == minimo_5:
            print 'El ganador de la Quinta carrera es: ' + str(ciclistas[i])
            break    

print '---------------------------------------------------' 

funcion_3(ciclistas,tiempo)    
    









