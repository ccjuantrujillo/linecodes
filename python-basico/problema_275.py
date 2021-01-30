def lista_perfecto(n):
    S=[]
    for var in range(1,n+1):
        sumatorio = 0
        for i in range(1,var):
            if var % i == 0:
                sumatorio += i
        if sumatorio == var:
            S.append(var)

    return S

limite = int(raw_input('Ingrese el numero n: '))

A=lista_perfecto(limite)

print A


            
        
    