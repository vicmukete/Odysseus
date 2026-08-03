import requests
import os

'''
present weather stats:

current temperature
current humidity
current description
current alert
'''
def get_current_weather(city_name):
    # key
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
            weather_data = response.json
            feels_like = weather_data["main"]["feels_like"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["main"][0]["Description"]

            # Alert Handler
            if "alerts" in weather_data and weather_data["alerts"]["alert"]:
                for alert in weather_data["alerts"]["alert"]:
                    alert_event = alert.get('event')
                    alert_severity = alert.get("severity")
                    alert_note = alert.get("note")
                print(f"ALERT, {alert_event}")


            # Print and Read
            print(f"Here's the weather for {city_name.title()}: ")
            print(f"FEELS LIKE, {feels_like}")
            print(f"TEMPERATURE,  {temperature}")
            print(f"HUMIDITY, {humidity}")
            print(f"DESCRIPTION,{description.capitalize()}")
            
        else:
            print(f"Error: Unable to fetch data. Status Code:{response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")


if __name__ == "__main__":
    # Should hold cpu read and interpreted 
    # value of designated city
    city = input("Enter city name: ")
    get_current_weather(city)