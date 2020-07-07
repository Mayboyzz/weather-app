import requests
from tkinter import *
from tkinter import ttk

# Creating the Window
root = Tk()
root.title('Weather App made by Christian')
mainframe = ttk.Frame(root)

def get_weather(city):
    weather_key = '1db1ab9a24c897ed0c0ebd6d3c726fb1'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}

    response = requests.get(url, params=params)
    print(response.json())

# Widgets
button = ttk.Button(root, text='Click ME!', command=get_weather)
button.pack()

entry = ttk.Entry(root)
entry.pack()

# Main Loop
flag = True

while flag:
    root.mainloop()