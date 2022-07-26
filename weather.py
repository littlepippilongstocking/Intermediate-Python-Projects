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
    weather_data = requests.get(base_url).json()
    pprint(weather_data)


if __name__ == '__main__':
    get_weather()
