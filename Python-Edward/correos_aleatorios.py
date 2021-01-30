from random import choice,randint


longitud_usuario_maxima = 10
longitud_dominio_maxima = 10
longitud_extension_maxima = 3

valores_usuario = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
valores_dominio = "0123456789abcdefghijklmnopqrstuvwxyz"
valores_extension = "abcdefghijklmnopqrstuvwxyz"



f = open ("lista.txt", "a")

for vuelta in range(0,100000):
	usuario = ""
	dominio = ""
	extension = ""


	usuario = usuario.join([choice(valores_usuario) for i in range(int(randint(1,longitud_usuario_maxima)))])
	#print(usuario)

	dominio = dominio.join([choice(valores_dominio) for i in range(int(randint(1,longitud_dominio_maxima)))])
	#print(dominio)

	extension = extension.join([choice(valores_extension) for i in range(int(randint(1,longitud_extension_maxima)))])
	#print(extension)

	correo_electronico = usuario + '@' + dominio + '.' + extension
	f.write(correo_electronico + "\n")
f.close()



