# created with AI assistance (you.com/chat) and OpenWeatherApi

import requests
from datetime import datetime

api = "9f2358a4637e058a3d95b06238572add"
location = input("Enter the city name: ")

fullapilink = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}"
apilink = requests.get(fullapilink)
data = apilink.json()

if data["cod"] == "404":
    print("Invalid city name.")
else:

    temperature = data["main"]["temp"]
    temp_c = round((temperature - 273.15), 2)
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])

    print(f"\nWeather Stats for {location.upper()} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Temperature: {temp_c} °C")
    print(f"Weather Description: {desc}")
    print(f"Humidity: {humidity}%")
    print(f"Sunrise Time: {sunrise}")
    print(f"Sunset Time: {sunset}")
