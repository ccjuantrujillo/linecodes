import smtplib, socket, sys, getpass

f = open("lista.txt")
for linea in f:
	# Conexion con el servidor 
	try:
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	        smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		print "Conexion exitosa con Gmail"
		print "Concectado a Gmail"
  		# Datos 
		try:
			gmail_user = 'puertosaber.mkting@gmail.com'
		        gmail_pwd = 'edward@lee123456'
                        smtpserver.login(gmail_user, gmail_pwd)
		except smtplib.SMTPException:
			print ""
			print "Autenticacion incorrecta" + "\n"
			smtpserver.close()
			getpass.getpass("Presione ENTER para continuar...")
		        sys.exit(1)
	except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
		print "Fallo en la conexion con Gmail"
		print getpass.getpass("Presione ENTER para continuar...")
		sys.exit(1)

	to = linea
	msg = 'Mensaje de Prueba de PYTHON'
	try:
		smtpserver.sendmail(gmail_user, to, msg)
	except smtplib.SMTPException:
		print "El correo no pudo ser enviado" + "\n"
		getpass.getpass("Presione ENTER para continuar...")
		sys.exit(1)
 
	print "El correo: " + linea + " Se envio correctamente" +"\n"
f.close()
smtpserver.close()