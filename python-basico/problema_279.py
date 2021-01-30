 #lista = [1,2,3]
#len(lista) = 3
#lista[0]=1
#lista[1]=2
#lista[2]=3

def series(lista):
    var = len(lista)
    for i in range(0,len(lista)-1):
        if lista[i]==lista[i+1]:
            var = var -1

    return var

print series([1,1,8,8,8,8,5])
            
        
        
    
