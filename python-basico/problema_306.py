def es_primo(n):
    sumatorio = 0
    for i in range(1,n+1):
        if n % i == 0:
            sumatorio = sumatorio + 1
    
    return sumatorio == 2

#print es_primo(7)

def tabla_primos(m):
    for i in range(1,m+1):
        if es_primo(i):
            print i, 'es un numero primo'

numero = int(raw_input('Ingrese un numero: '))

tabla_primos(numero)