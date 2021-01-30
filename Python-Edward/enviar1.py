import smtplib

f = open("lista.txt")
for linea in f:
	fromaddr = 'puertosaber.mkting@gmail.com'
	toaddrs  = linea
	msg = 'Correo enviado utilizano Python'
 
 
	# Datos
	username = 'puertosaber.mkting@gmail.com'
	password = 'edward@lee123456'
 
	# Enviando el correo
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
f.close()