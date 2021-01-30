import smtplib
 
fromaddr = 'puertosaber.mkting@gmail.com'
toaddrs  = 'juanperezuni123456@gmail.com'
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