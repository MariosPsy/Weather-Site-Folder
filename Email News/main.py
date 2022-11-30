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
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}" \
      "&from=2022-10-30&sortBy=publishedAt" \
      "&apiKey=b2c2b8a40ae144a28bf4a74f4390bdfc" \
      "&Language=en"

requests = requests.get(url)
content = requests.json()
print(content)



message = """Subject: Email News for Tesla""" + "\n"

for article in content["articles"][0:5] :
    if (article["title"] is not None) and (article["description"] is not None) :
        # print(article["title"])
        # print(article["description"])
        message = message + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"]+ 2*"\n"

print(message)

message = message.encode("utf-8")

email_senter(message)




