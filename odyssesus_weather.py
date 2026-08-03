import requests
import os

def get_weather(city):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   
    query_parameters = {
        "q": city_name,
        "aapid": api_key,
        "units": "metric"
    }    

    try:
        response = requests.get(url, params=query_parameters)

        if response.status_code == 200:
            weather_data = response.json()
            feels_like = weather_data["main"]["feels_like"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["main"][0]["Description"]

            print(f"Here's the weather for {city_name.title()}: ")
            print(f"It FEELS LIKE: {feels_like}")
            print(f"With a TEMPERATURE of : {temperature}")
            print(f"And HUMIDITY of : {humidity}")
            print(f"Here's your DESCRIPTION: {description}")
        else:
            print(f"Error: Unable to fetch data. Status Code:{response.status_code}")



    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")

