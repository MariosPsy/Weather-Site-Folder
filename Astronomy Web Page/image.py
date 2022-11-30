import requests

def image_downloader(url) :
    response = requests.get(url)
    with open("image.jpg", "wb") as file :
        file.write(response.content)

image_downloader("https://api.nasa.gov/assets/img/general/apod.jpg")