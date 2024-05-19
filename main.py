import requests

from apikey import API_TOKEN

start = True

while start:

    city = input("Город: ")

    params = {
        "q" : city,
        "appid" : API_TOKEN,
        "units" : "metric"
    }

    if city.lower() == "exit":
        start = False
    else:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        x = response.json()
        print(f"Погода - {x["weather"][0]['description']}")
        print(f"Максимальная температура - {int(x["main"]['temp_max'])} °C, минимальная - {int(x["main"]['temp_min'])} °C")
