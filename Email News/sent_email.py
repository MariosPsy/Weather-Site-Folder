import smtplib, ssl

host = "smtp.gmail.com" #Default arguments for gmail
port = 465

username = "marious.ps@gmail.com"
password = "ehopwycdwiekempo"

receiver = "marious.ps@gmail.com"

#Create a secure contex
contex = ssl.create_default_context()

message = """Subject: From Python Script mail 
Hello from python script
It is unbelievable
Goodby
"""
with smtplib.SMTP_SSL(host, port, context=contex) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)