#!bin/bash/python5

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("sourabhmvmo@gmail.com", "iamiRonman#24@")
subject = 'web site error'

msg = "There is somthing wrong in your code"

server.sendmail("sourabhmvmo@gmail.com", "sourabhclasher@gmail.com", msg)
print("Email sent successfully!")
server.quit()
