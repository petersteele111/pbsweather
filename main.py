from dotenv import load_dotenv
import os
import requests
import tkinter
import tkinter.messagebox
import customtkinter


# Static Methods
def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


# GetWeather Class
class GetWeather:
    def __init__(self, zipcode):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.base_url = "https://api.weatherapi.com/v1"
        self.zipcode = zipcode

        self.params = {"key": self.api_key, "q": self.zipcode, "days": 3}

        self.response = requests.get(self.base_url + "/current.json", params=self.params)

        self.data = self.response.json()


class SideBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # App Name
        self.app_name = customtkinter.CTkLabel(master=self, text="Get Weather", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.app_name.grid(row=0, column=0, padx=10, pady=10)

        # Zipcode Entry
        self.zipcode_entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter Zipcode")
        self.zipcode_entry.grid(row=1, column=0, pady=(0, 10))

        # Search Button
        self.search_button = customtkinter.CTkButton(master=self, text="Search", command=self.get_weather)
        self.search_button.grid(row=2, column=0, padx=10, pady=10)

        # Label for Appearance Mode
        self.appearance_mode_label = customtkinter.CTkLabel(master=self, text="Appearance Mode")
        self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=10)

        # Option Menu to change light and dark mode
        self.theme_option_menu = customtkinter.CTkOptionMenu(master=self, values=["Dark", "Light", "System"], command=change_appearance_mode_event)
        self.theme_option_menu.grid(row=6, column=0, padx=10, pady=10)

        # Exit Button
        self.exit_button = customtkinter.CTkButton(master=self, text="Exit", command=self.quit)
        self.exit_button.grid(row=7, column=0, padx=10, pady=10)

    # write function to get the input zipcode from the CTkEntry and then use that to get the weather
    def get_weather(self):
        zipcode = self.zipcode_entry.get()
        weather_data = GetWeather(zipcode).data
        self.master.update_weather(weather_data)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("PBS Weather App")
        # self.geometry("1000x1200")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar_frame = SideBarFrame(master=self, width=400, height=1000)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", rowspan=10)

        self.weather = GetWeather(49788)

        # create weather frame
        self.weather_frame = customtkinter.CTkFrame(master=self)
        self.weather_frame.grid(row=0, column=1, padx=10, sticky="nsew")

        # Show the current location name from weather
        self.current_location_text = customtkinter.CTkLabel(master=self.weather_frame, text="Location: " + self.weather.data["location"]["name"] + ", " + self.weather.data["location"]["region"] + " " + self.weather.data["location"]["country"], font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_location_text.grid(row=0, column=1, padx=10, pady=10, sticky="NW")

        # Show the current conditions from weather
        self.current_conditions_text = customtkinter.CTkLabel(master=self.weather_frame, text="Current Conditions: " + self.weather.data["current"]["condition"]["text"], font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_conditions_text.grid(row=1, column=1, padx=10, pady=10, sticky="NW")

        # Show the current temperature from weather
        self.current_temperature = customtkinter.CTkLabel(master=self.weather_frame, text="Current Temp: " + str(self.weather.data["current"]["temp_f"]) + "°F", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_temperature.grid(row=2, column=1, padx=10, pady=10, sticky="NW")

        # Show the current feels like from weather
        self.current_feels_like = customtkinter.CTkLabel(master=self.weather_frame, text="Current Feels Like: " + str(
            self.weather.data["current"]["feelslike_f"]) + "°F", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_feels_like.grid(row=3, column=1, padx=10, pady=10, sticky="NW")

        # Show the current humidity from weather
        self.current_humidity = customtkinter.CTkLabel(master=self.weather_frame, text="Current Humidity: " + str(self.weather.data["current"]["humidity"]) + "%", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_humidity.grid(row=4, column=1, padx=10, pady=10, sticky="NW")

        # Show the current wind speed from weather
        self.current_wind_speed = customtkinter.CTkLabel(master=self.weather_frame, text="Current Wind Speed: " + str(self.weather.data["current"]["wind_mph"]) + "mph", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_wind_speed.grid(row=5, column=1, padx=10, pady=10, sticky="NW")

        # Show the current wind direction from weather
        self.current_wind_direction = customtkinter.CTkLabel(master=self.weather_frame, text="Current Wind Direction: " + str(self.weather.data["current"]["wind_dir"]), font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_wind_direction.grid(row=6, column=1, padx=10, pady=10, sticky="NW")

        # Show the current pressure from weather
        self.current_pressure = customtkinter.CTkLabel(master=self.weather_frame, text="Current Pressure: " + str(self.weather.data["current"]["pressure_mb"]) + "mb", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_pressure.grid(row=7, column=1, padx=10, pady=10, sticky="NW")

        # Show the current precipitation from weather
        self.current_precipitation = customtkinter.CTkLabel(master=self.weather_frame, text="Current Precipitation: " + str(self.weather.data["current"]["precip_in"]) + "in", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_precipitation.grid(row=8, column=1, padx=10, pady=10, sticky="NW")

        # Show the current cloud cover from weather
        self.current_cloud_cover = customtkinter.CTkLabel(master=self.weather_frame, text="Current Cloud Cover: " + str(self.weather.data["current"]["cloud"]) + "%", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_cloud_cover.grid(row=9, column=1, padx=10, pady=10, sticky="NW")

        # Show the current UV from weather
        self.current_uv = customtkinter.CTkLabel(master=self.weather_frame, text="Current UV: " + str(self.weather.data["current"]["uv"]), font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_uv.grid(row=10, column=1, padx=10, pady=10, sticky="NW")

        # Show the current visibility from weather
        self.current_visibility = customtkinter.CTkLabel(master=self.weather_frame, text="Current Visibility: " + str(self.weather.data["current"]["vis_miles"]) + "mi", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_visibility.grid(row=11, column=1, padx=10, pady=10, sticky="NW")

        # Show the current last updated from weather
        self.current_last_updated = customtkinter.CTkLabel(master=self.weather_frame, text="Current Last Updated: " + str(self.weather.data["current"]["last_updated"]), font=customtkinter.CTkFont(size=14, weight="bold"))
        self.current_last_updated.grid(row=12, column=1, padx=10, pady=10, sticky="NW")



    def update_weather(self, weather_data):
        # update the location
        self.current_location_text.configure(
            text="Location: " + weather_data["location"]["name"] + ", " + weather_data["location"][
                "region"] + " " + weather_data["location"]["country"])

        # update the current conditions
        self.current_conditions_text.configure(
            text="Current Conditions: " + weather_data["current"]["condition"]["text"])

        # update the current temperature
        self.current_temperature.configure(text="Current Temp: " + str(weather_data["current"]["temp_f"]) + "°F")

        # update the current feels like
        self.current_feels_like.configure(
            text="Current Feels Like: " + str(weather_data["current"]["feelslike_f"]) + "°F")

        # update the current humidity
        self.current_humidity.configure(text="Current Humidity: " + str(weather_data["current"]["humidity"]) + "%")

        # update the current wind speed
        self.current_wind_speed.configure(
            text="Current Wind Speed: " + str(weather_data["current"]["wind_mph"]) + "mph")

        # update the current wind direction
        self.current_wind_direction.configure(
            text="Current Wind Direction: " + str(weather_data["current"]["wind_dir"]))

        # update the current pressure
        self.current_pressure.configure(
            text="Current Pressure: " + str(weather_data["current"]["pressure_mb"]) + "mb")

        # update the current precipitation
        self.current_precipitation.configure(
            text="Current Precipitation: " + str(weather_data["current"]["precip_in"]) + "in")

        # update the current cloud cover
        self.current_cloud_cover.configure(
            text="Current Cloud Cover: " + str(weather_data["current"]["cloud"]) + "%")

        # update the current UV
        self.current_uv.configure(text="Current UV: " + str(weather_data["current"]["uv"]))

        # update the current visibility
        self.current_visibility.configure(
            text="Current Visibility: " + str(weather_data["current"]["vis_miles"]) + " miles")

        # update the current last updated
        self.current_last_updated.configure(
            text="Current Last Updated: " + str(weather_data["current"]["last_updated"]))


if __name__ == "__main__":
    app = App()
    app.mainloop()

