import requests


def find_weather():
    API_KEY = "abeb3a0ce0e0a68522b30069143cf645"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = 'Faridabad, Haryana'
    request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
    response = requests.get(request_url)

    if response.status_code == 200:
        json_result = response.json()
        print(json_result)

        weather_main = json_result['weather'][0]['main']
        weather_desc = json_result['weather'][0]['description']

        tempC = int(json_result['main']['temp'] - 273.15)
        tempF = int((json_result['main']['temp'] - 273.15) * 9/5 + 32)

        humidity = json_result['main']['humidity']

        visibilty = json_result['visibility'] / 1000 # it will be given in m but is converted into km after division

        det = f"""
weather: {weather_main}
weather-desc: {weather_desc}
temp: {tempC}
humidity: {humidity}
visibility: {visibilty} km"""
        
        return det

    else:
        print('We are unable to reach weather data right now, please try again later', response.status_code)


print(find_weather())