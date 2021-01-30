def saludar(nombre):
    print("Hola ",nombre)

def bienvenida(nombre):
    print("Hola ",nombre, " Bienvenido a la fiesta")

def despedir(nombre):
    print("Adios ",nombre)

print("Ingresar nombre:")
nombre = input()

saludar(nombre)
bienvenida(nombre)
despedir(nombre)