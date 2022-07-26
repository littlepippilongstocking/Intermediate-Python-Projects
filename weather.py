"""
Dilyana Koleva, July 2022
Simple function to get the weather for any city in the world
The data is printed in json format so pprint is necessary to make it more readble

To access the API key make an account in : https://openweathermap.org/

"""
import requests
from pprint import pprint


def get_weather():
    API_key = ''  # Add your API key here
    city = input("Please enter a city: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?&q=" + city + "&appid=" + API_key
    weather_data = requests.get(base_url).json()['main']
    temp = weather_data['temp']
    feels_like = weather_data['feels_like']
    temp_min = weather_data['temp_min']
    temp_max = weather_data['temp_max']
    pressure = weather_data['pressure']
    humidity = weather_data['humidity']
    print(f"Welcome to {city}. The temperature here today is {temp} degrees, but it feels like {feels_like} degrees.\n"
          f"The maximum temperature would be {temp_max} degrees and the minimum : {temp_min} degrees.\n"
          f"The pressure and humidity are respectively {pressure} hPa and {humidity}%.")


if __name__ == '__main__':
    get_weather()
