import requests
import api

print("\n" + "Hello from image downloader" + "\n")

image_url = api.content["hdurl"]
response = requests.get(image_url)
with open("image.jpg", "wb") as file :
    file.write(response.content)
