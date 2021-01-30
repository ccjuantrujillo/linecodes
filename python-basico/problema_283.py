#lista = [1,2,3]
#len(lista) = 3
#lista[0]=1
#lista[1]=2
#lista[2]=3

def valor_absoluto(valor):
    if valor > 0:
        resultado = valor
    else:
        resultado = -1.0 * valor

    return resultado


def maxima_serie(lista):
    B=[]
    for i in range(0,len(lista)-1):
        B.append(valor_absoluto(lista[i+1]-lista[i]))

    return max(B)

print maxima_serie([1,10,2,6,2,0])
        
        