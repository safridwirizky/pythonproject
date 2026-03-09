import smtplib, os

my_mail = "prjctpy@gmail.com"
password = os.getenv("PRJCTPY_PASSWORD")

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_mail, password=password)
connection.sendmail(
    from_addr=my_mail,
    to_addrs="zz_zz93@yahoo.com",
    msg="Subject:Hello Safri\n\nAku lagi coba smtp."
)
connection.close()