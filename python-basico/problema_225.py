n = int(raw_input('Ingrese el valor de n: '))

a = range(1,n)

for aux in range(0,len(a)):
    a[aux] = a[aux]*a[aux]

for aux in range(0,len(a)):
    print a[aux]
    