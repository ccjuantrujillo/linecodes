def cuota_mensual(h,n,i):
    r = i/(100*12)
    m = h*r/(1.0-(1.0+r)**(-1.0*12*n))
    return round(m,2)

print cuota_mensual(150000,15,4.75)
    