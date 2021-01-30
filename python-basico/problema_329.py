def cuota_mensual(h,n,i):
    r = i/(100*12)
    m = h*r/(1.0-(1.0+r)**(-1.0*12*n))
    return round(m,2)

def total_pagado(h,n,i):
    var_aux= cuota_mensual(h,n,i)
    resultado = 12.0*n*var_aux
    return round(resultado,2)

def interes(h,n,i):
    var_aux_2 = total_pagado(h,n,i)
    resultado = var_aux_2 - h
    return resultado

def porcentaje(h,n,i):
    var_aux = interes(h,n,i)
    resultado = var_aux*(100.0/h)
    return round(resultado,2)

print 'El total pagado para 10 aos es:', total_pagado(150000,10,4.75)
print 'El total pagado para 15 aos es:',total_pagado(150000,15,4.75)
print 'El total pagado para 20 aos es:',total_pagado(150000,20,4.75)
print 'El total pagado para 25 aos es:',total_pagado(150000,25,4.75)