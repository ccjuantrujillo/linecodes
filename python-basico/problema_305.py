def entero_invertido(numero):
    variable = str(numero)[::-1]
    for i in range(len(variable)):
        print variable[i]
    


print entero_invertido(1234)