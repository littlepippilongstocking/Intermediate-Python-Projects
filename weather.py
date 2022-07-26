"""
Dilyana Koleva, July 2022
Simple function to get the weather for any city in the world
The data is printed in json format so pprint is necessary to make it more readble

To access the API key make an account in : https://openweathermap.org/

"""
import requests
from pprint import pprint


def get_weather():
    API_KEY = ''  # Add your API key here
    city = input("Please enter a city: ")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?&q=" + city + "&appid=" + API_KEY
    weather_data = requests.get(BASE_URL).json()['main']

    temp = round(weather_data['temp'] - 273.15, 2)
    feels_like = round(weather_data['feels_like'] - 273.15, 2)
    temp_min = round(weather_data['temp_min'] - 273.15, 2)
    temp_max = round(weather_data['temp_max'] - 273.15, 2)
    pressure = weather_data['pressure']
    humidity = weather_data['humidity']

    print(f"Welcome to {city}. The temperature here today is {temp} degrees, but it feels like {feels_like} degrees.\n"
          f"The maximum temperature would be {temp_max} degrees and the minimum : {temp_min} degrees.\n"
          f"The pressure and humidity are respectively {pressure} hPa and {humidity}%.")


if __name__ == '__main__':
    get_weather()
