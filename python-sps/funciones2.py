#Serie de fibonacci
n = int(input('Ingrese el tamaño de la serie'))
lista = []
anterior_a = 0
anterior_z = 1
lista.append(anterior_a)
lista.append(anterior_z)
for i in range(n):
    actual = anterior_a + anterior_z
    lista.append(actual)
    anterior_a = anterior_z
    anterior_z = actual

print(lista)