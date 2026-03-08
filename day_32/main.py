import smtplib

my_mail = "ujicobamailpython772@gmail.com"
password = "123"

connection = smtplib.SMTP("smtp.google.com")
connection.starttls()
connection.mail()
connection.close()