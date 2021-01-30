n = float(raw_input('Ingrese el valor de n: '))
m = float(raw_input('Ingrese el valor de m: '))

factorial_n = 1
factorial_m = 1
factorial_n_m  = 1

i=1
j=1
k=1
#factorial de n
while i<=n:
    factorial_n = factorial_n * i
    i += 1
#factorial de m
while j<=m:
    factorial_m = factorial_m * j
    j += 1
#factorial de n-m
while k<=(n-m):
    factorial_n_m = factorial_n_m * k
    k += 1

resultado = float(factorial_n/(factorial_m*factorial_n_m))

print resultado
