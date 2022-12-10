import requests

API_KEY = "c8a28f3b2d1ebeff795a3b4edcaa6395"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nm_values = 8 * forecast_days
    filtered_data = filtered_data[:nm_values]
    if kind == "Temperature" :
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky" :
        filtered_data = [dict[]]
    return content

if __name__ == "__main__":
    print(get_data("Athens"))