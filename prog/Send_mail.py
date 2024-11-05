import smtplib
from secrets import login, password

email_from = "From: Bolotov"
email_to = "To: Kuzovkov"
message = "Hello"

server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()