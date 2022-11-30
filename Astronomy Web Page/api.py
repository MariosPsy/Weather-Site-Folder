import requests

api = "EeKwoKkOpaZjoKQs3FdxQFd1GZ5S9Lh1i3UmrcS9"

url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

request = requests.get(url)
content = request.json()
print(content)
title = content["title"]
text = content["explanation"]
print("TITLE" + "\n" + title + "\n")
print("TEXT" + "\n" + text + "\n")
