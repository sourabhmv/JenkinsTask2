#!bin/bash/python3

import smtplib

server=smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()

server.login("sourabhclasher@gmail.com", "CLASHEr#24@")
subject = "Error in your web site"

msg = "Web site is not working"

server.sendmail("sourabhclasher@gmail.com", "sourabhmvmo@gmail.com", msg)
print("Email sent successfully!")
server.quit()
