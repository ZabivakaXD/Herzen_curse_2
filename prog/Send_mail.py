import smtplib
from secrets import login, password

email_from = login
email_to = "kbolotov2004@gmail.com"
subject = 'Test'
message = "Hello"

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, f'Subject:{subject}\n{message}')
server.quit()