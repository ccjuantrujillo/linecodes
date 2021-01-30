#lista = [1,2,3]
#len(lista) = 3
#lista[0]=1
#lista[1]=2
#lista[2]=3

def sumatorio(lista):
    S=[]
    for i in range(0,len(lista)-1):
        S.append(lista[i+1]-lista[i])
    return sum(S)

print sumatorio([1,3,6,10,11,2,34])

