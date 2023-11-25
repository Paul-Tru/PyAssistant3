import requests
import datetime
import json
from tabulate import tabulate
from functions.tools import tools

api_key = ''
city_name = tools.config_var("openweathermap", "city_name")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=de&limit=50'
weather_continue = []

try:
    while True:
        data = requests.get(url).json()
        date = datetime.datetime.now().strftime("%D.%m.%Y|%H:%M")

        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        temp = round(data['main']['temp'], 1)
        feels_like = round(data['main']['feels_like'], 1)
        humidity = data['main']['humidity']
        visi = data['visibility']
        windms = data["wind"]["speed"]
        wind = round(windms * 3.6, 2)
        weather_des = data["weather"][0]["description"]
        clouds = data['clouds']['all']

        weather_data = {
            "temperature": temp,
            "humidity": humidity,
            "date": date
        }

        weather_list = [
            ["Temperatur", temp],
            ["Gefühlt", feels_like],
            ["Feuchtigkeit", humidity],
            ["Windgeschwindigkeit", wind],
            ["Sicht", visi],
            ["Wetter", weather_des],
            ["Sonnenaufgang", sunrise],
            ["Sonnenuntergang", sunset],
            ["Wolken", clouds]
        ]

        if weather_list not in weather_continue:
            print("\r", end="")
            weather_continue.append(weather_list)
            table = tabulate(weather_list,headers=["Titel", "Wert"], tablefmt="pipe")
            print(table)
            print()

except Exception as e:
    print("Fehler:", str(e))
