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

app = customtkinter.CTk()

app.title("PBS Weather App")
app.geometry("1000x1000")

city = tkinter.Label(master=app, text="Enter a city name:")
city.pack()
city_name = tkinter.Entry(master=app)
city_name.pack()

frame = customtkinter.CTkFrame(master=app, width=400, height=200)
frame.pack()

label = customtkinter.CTkLabel(master=app, text="Current weather in " + location["name"] + ", " + location["region"] + ":")
label.pack()

temp = customtkinter.CTkLabel(master=app, text=str(current["temp_f"]) + "°F and " + current["condition"]["text"])
temp.pack()

feels_like = customtkinter.CTkLabel(master=app, text="Feels like " + str(current["feelslike_f"]) + "°F")
feels_like.pack()

wind = customtkinter.CTkLabel(master=app, text="Wind: " + str(current["wind_mph"]) + " mph " + current["wind_dir"])
wind.pack()

pressure = customtkinter.CTkLabel(master=app, text="Pressure: " + str(current["pressure_mb"]) + " mb")
pressure.pack()

humidity = customtkinter.CTkLabel(master=app, text="Humidity: " + str(current["humidity"]) + "%")
humidity.pack()

uv = customtkinter.CTkLabel(master=app, text="UV: " + str(current["uv"]))
uv.pack()

cloud = customtkinter.CTkLabel(master=app, text="Cloud: " + str(current["cloud"]) + "%")
cloud.pack()

visibility = customtkinter.CTkLabel(master=app, text="Visibility: " + str(current["vis_miles"]) + " mi")
visibility.pack()

app.mainloop()
