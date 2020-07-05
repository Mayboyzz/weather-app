import requests

def get_weather(city):
    weather_key = '1db1ab9a24c897ed0c0ebd6d3c726fb1'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}

    response = requests.get(url, params=params)
    print(response.json())

get_weather('Sulphur')