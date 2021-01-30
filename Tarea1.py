#Codifique un programa que permita el ingreso de un texto, que solo contenga
#letras, espacios en blanco, comas el cual debe terminmar en un punto.
import re
from array import array

valido = True
mensaje = ""

def encripta(cad):
    equi = {"M":0,"u":1,"r":2,"a":5,"c":7}
    cad2 = ""
    for i in cad:
        cad2 += i
    return cad2

while(valido):
    valido = False
    cadena = input("Ingrese una cadena: ")
    for i in cadena:
        if not re.match("[a-z A-Z,]+",i):
            valido = True
            mensaje = 'Su cadena contiene un caracter invalido ' + i
            break
    if valido:
        print(mensaje)

print("Cadena Ingresada: " + cadena)
print("Cadena encriptada: " + encripta(cadena))

