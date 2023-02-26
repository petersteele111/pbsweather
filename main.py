from dotenv import load_dotenv
import os
import requests
import tkinter
import tkinter.messagebox
import customtkinter

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.weatherapi.com/v1"
city = 49788

params = {"key": api_key, "q": city, "days": 3}

response = requests.get(base_url + "/current.json", params=params)

data = response.json()

location = data["location"]
current = data["current"]

print(f"Current weather in {location['name']}, {location['region']}:")
print(f"{current['temp_f']}°F and {current['condition']['text']}")
print(f"Feels like {current['feelslike_f']}°F")
print(f"Wind: {current['wind_mph']} mph {current['wind_dir']}")
print(f"Pressure: {current['pressure_mb']} mb")
print(f"Humidity: {current['humidity']}%")
print(f"UV: {current['uv']}")
print(f"Cloud: {current['cloud']}%")
print(f"Visibility: {current['vis_miles']} mi")