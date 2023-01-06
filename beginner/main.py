import yagmail
# This is the mail of your account / Este es el correo de tu cuenta
email = "santiagofontanaagithub@gmail.com"
# You will get this password by creating an app password from Google / Esta contraseña la conseguiras creando una contraseña de app desde Google
password = "urlhqhxefymhjgci"

yag = yagmail.SMTP(user=email, password=password)

to = ['contactosantiagocfon@gmail.com']
subject = "subject"
html = 'main.html'

yag.send(to = to, subject = subject, contents = html)