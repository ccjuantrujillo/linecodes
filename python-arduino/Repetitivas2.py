n = int(input("Ingrese un numero: "))
prod = 1
while(n>0):
    prod *= n
    n -= 1
print("El factorial es: {} ".format(prod))