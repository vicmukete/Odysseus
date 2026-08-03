import requests
import os
from datetime import date, datetime, timedelta

'''
present weather stats:

current temperature
current humidity
current description
current alert
'''

api_key = os.getenv("API_KEY")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   
def get_current_weather(city_name):
    # key

    query_parameters = {
        "q": city_name,
        "aapid": api_key,
        "units": "metric",
        "alerts": "yes"
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
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        
    except Exception as err:
        print(f"Unkown error occured: {err}")
    



def get_forecasted_weather(city_name):

    querey_parameters = {
        "q": city_name,
        "aapid": api_key,
        "units": "metrics",
        "days": num_days
    }

    # YYYY-MM-DD
    today = date.today()
    tomrrow = date.today() + timedelta(days=1)

    # Could do (requested day - current day)
    if today:
        num_days = 1

    try:
        response = requests.get(url, querey_parameters)

        if response.status_code == 200:
            weather_data = response.json()
            forecast_days = weather_data["forecast"]["forecastday"]
            for day in forecast_days:
                date = day["date"]

                day_info = day["day"]
                max_temp = day_info["maxtemp_f"]
                min_temp = day_info["mintemp_f"]
                condition = day_info["condition"]["text"]
                avg_humidity = day_info["avghumidity"]

                # Alerts
                if "alerts" in weather_data and weather_data["alerts"]["alert"]:
                    for alert in weather_data["alerts"]["alert"]:
                        alert_event = alert.get('event')
                        alert_severity = alert.get("severity")
                        alert_note = alert.get("note")
                    print(f"ALERT, {alert_event}")


                print(f"DATE, {date}")
                print(f"CONDITION, {condition}")
                print(f"MAX TEMP, {max_temp}")
                print(f"MIN_TEMP, {min_temp}")
                print(f"AVERAGE HUMIDITY, {avg_humidity}")

        else:
            print(f"Error: Unable to fetch data. Status Code:{response.status_code}")
            


    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"Unkown error occured: {err}")




if __name__ == "__main__":

# determine how/when to run either current ore forecasted



    # Should hold cpu read and interpreted 
    # value of designated city
    # city_name query
    city = input("Enter city name: ")
    get_current_weather(city)
    get_forecasted_weather(city)