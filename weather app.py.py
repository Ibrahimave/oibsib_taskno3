import datetime as dt

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "00d2a97757d5eb1a9967035223265bed"
CITY = "delhi"


def kelvin_to_celsius_fahrenheit(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9 / 5) + 32
  return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['temp']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(
    feels_like_kelvin)
wind_speed = response['main']['humidity']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] +
                                            response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] +
                                           response['timezone'])

print(f"temperature in {CITY}:{temp_celsius:.2f}°C or {temp_fahrenheit:.2F}°F")
print(
    f"temperature in {CITY}feels_like:{temp_celsius:.2f}°C or {temp_fahrenheit:.2F}°F"
)
print(f"humidity in {CITY}:{humidity}%")
print(f"wind speed in {CITY}:{wind_speed}m/s")
print(f"general weather in {CITY}:{description}")
print(f"sun rise in {CITY}at{sunrise_time} local time.")
print(f"sun sets in {CITY}at{sunset_time}local time.")
