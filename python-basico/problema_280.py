#lista = [1,2,3]
#len(lista) = 3
#lista[0]=1
#lista[1]=2
#lista[2]=3


    for i in range(0,len(lista)-1):
        if lista[i]==lista[i+1]:
            var = var + 1
        else:
            B.append(var)
            var=1
    var = 1        
    for i in range(len(lista)-1,0,-1):
        if lista[i]==lista[i-1]:
            var = var + 1
        else:
            B.append(var)
            break
        
    return B

print maxima_serie([1,1,8,8,8,8,2,2,2,2,2,2,2,1,1,1,2,2,2,2])

                
            