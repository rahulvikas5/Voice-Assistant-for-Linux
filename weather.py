import requests
from sp_function import *

api_key = 'a4b621a7669e473e3b2f0613217fa009'


def get_weather():
    print('Linux Assistant: Speak the city name only!')
    g_speak('Speak the city name')
    city = takeCommand()

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp'] - 273.15
        rt = round(temp)
        desc = data['weather'][0]['description']
        print(f'Linux Assistant: Temperature: {rt} C. The scene looks {desc}')
        g_speak(f"The temperature is {rt} degree celsius and the scene looks {desc}")

    else:
        print('Error fetching weather data of selected city')
        g_speak('Error fetching weather data')
