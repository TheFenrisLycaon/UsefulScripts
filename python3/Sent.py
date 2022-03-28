import smtplib

fadd = ""
tadd = ""
msg = "Mail sent through Python!"
username = ""
password = ""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, msg)
