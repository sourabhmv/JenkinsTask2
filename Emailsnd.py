#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("sender_mail", "password")

msg = "There is somthing wrong in your code"

server.sendmail("sender_mail", "receiver_mail", msg)
print("Email sent successfully!")
server.quit()
