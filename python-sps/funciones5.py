#Diccionarios
type(5)
regiones = {"Lima":30,"Huancayo":15,"Arequips":12}
print(regiones)
print(regiones["Arequips"])

for a,b in regiones.items():
    if b == 15:
        print(a)
