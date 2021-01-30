cantidad = int(raw_input('Ingrese la cantidad: '))

for billete in [500,200,100,50,20,10,5,2,1]:
    
    cantidad = cantidad - (cantidad%billete)
    if cantidad > 0:
        variable  = int(cantidad/billete)
        print 'la cantidad del billete',billete,'es',variable,''
    else:
        break
        
    