import requests
import smtplib, ssl

def email_senter(message) :
    host = "smtp.gmail.com"  # Default arguments for gmail
    port = 465

    username = "marious.ps@gmail.com"
    password = "ehopwycdwiekempo"

    receiver = "marious.ps@gmail.com"

    # Create a secure contex
    contex = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=contex) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

api = "b2c2b8a40ae144a28bf4a74f4390bdfc"
url = """https://newsapi.org/v2/everything?q=tesla&from=2022-10-28&sortBy=publishedAt&apiKey=b2c2b8a40ae144a28bf4a74f4390bdfc"""

requests = requests.get(url)
content = requests.json()
print(content)

message = host = "smtp.gmail.com" #Default arguments for gmail
port = 465

username = "marious.ps@gmail.com"
password = "ehopwycdwiekempo"

receiver = "marious.ps@gmail.com"

#Create a secure contex
contex = ssl.create_default_context()

message = """Subject: Email News for Tesla""" + "\n"

for article in content["articles"] :
    # print(article["title"])
    # print(article["description"])
    message += article["title"] + "\n" + article["description"] + "\n" + "\n"

print(message)

email_senter(message)




