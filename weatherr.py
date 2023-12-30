import requests
from plyer import notification
import datetime

def greet_user():
    API_KEY = "abeb3a0ce0e0a68522b30069143cf645"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    city = 'Faridabad, Haryana'
    request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
    response = requests.get(request_url)

    if response.status_code == 200:
        json_result = response.json()

        weather_main = json_result['weather'][0]['main']
        weather_desc = json_result['weather'][0]['description']

        tempC = int(json_result['main']['temp'] - 273.15)
        tempF = int((json_result['main']['temp'] - 273.15) * 9/5 + 32)

        humidity = json_result['main']['humidity']

        visibilty = json_result['visibility'] / 1000 # it will be given in m but is converted into km after division
        
        hours = datetime.datetime.now().hour

        if hours >= 0 and hours < 12:
            title = "Good morning"
        elif hours >= 12 and hours < 17:
            title = 'Good afternoon'
        else:
            title = "Good evening"

        notification.notify(
title=title,
message=f"""
Temperature: {tempC}oCelsuis {tempF}oF
Weather: {weather_main}
""",
app_name='Lenovo',
timeout=5,
toast=False
)

    else:
        return f"We are unable to reach weather data right now, please try again later, {response.status_code}. We are trying our best."
    