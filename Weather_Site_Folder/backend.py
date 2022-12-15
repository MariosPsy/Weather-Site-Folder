import requests

API_KEY = "c8a28f3b2d1ebeff795a3b4edcaa6395"

def get_data(place, forecast_days=1, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nm_values = 8 * forecast_days
    filtered_data = filtered_data[:nm_values]
    filtered_content = filtered_data[:nm_values]
    # print(filtered_content)
    if kind == "Temperature" :
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky" :
        pass
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data, filtered_content

if __name__ == "__main__":
    print(get_data("Athens", 1, "Temperature"))