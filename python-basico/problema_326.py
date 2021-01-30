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

print interes(150000,15,4.75)