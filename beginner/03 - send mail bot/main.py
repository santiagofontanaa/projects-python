import yagmail
# This is the mail of your account / Este es el correo de tu cuenta
email = "santiagofontanaagithub@gmail.com" # This is my testing email, you need to put your own mail
# You will get this password by creating an app password from Google / Esta contraseña la conseguiras creando una contraseña de app desde Google
password = "***" 

# This is the connection with the Gmail / Esta es la conexión con la base de datos
yag = yagmail.SMTP(user=email, password=password)

# Here we put the receiver, subject and html page / Aquí ponemos el receptor, sujeto y página html
to = ['contactosantiagocfon@gmail.com'] 
subject = "Test of Sending mails with Python"
html = 'index.html'

# Here we send the mail / Aquí enviamos el correo electrónico
yag.send(to = to, subject = subject, contents = html)
