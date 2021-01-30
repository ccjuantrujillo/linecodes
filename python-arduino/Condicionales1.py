print("Hola mundo")
a = "hola"
print(a)
lista = [2,7,8,6,3,9,"hola"]
a1=[2,3.5,"hola"]
print(a1)
print(type(a1))
#Las listas
a1[0]=100
#Las tuplas no se pueden modificar
b = (2,3,4,"hola")
print(b[2])
print(b[0:4:2])#inicio|final|paso
#Diccionarios
c="ahola"
print(c*2)
d=[1,2,3]
print(d+d)
print("")
matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]

matriz[1][3]=6
matriz[3][3]=12

print(matriz)

cadena = "zeréP nauJ,01"
print(cadena[11::-1])
print(cadena[::])
