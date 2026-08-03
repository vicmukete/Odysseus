import requests
import os
from datetime import timedelta
import traceback

from dotenv import load_dotenv
load_dotenv()


'''
present weather stats:

current temperature
current humidity
current description
current alert
'''

#key
weather_api_key = os.getenv("WEATHER_API_KEY")
url = "http://api.weatherapi.com/v1/current.json"

   
def get_current_weather(city_name):
    

    
    query_parameters = {
        "key": weather_api_key,
        "q": city_name,
        "aqi": "no"
    }    

    try:
        response = requests.get(url, params=query_parameters)

        if response.status_code == 200:
            weather_data = response.json()
            current = weather_data["current"]

            feels_like = current["feelslike_f"]
            temperature = current["temp_f"]
            humidity = current["humidity"]
            description = current["condition"]["text"]


            # Print and Read
            print(f"\nHere's the weather for {city_name.title()}: ")
            print(f"FEELS LIKE, {feels_like}")
            print(f"TEMPERATURE,  {temperature}")
            print(f"HUMIDITY, {humidity}")
            print(f"DESCRIPTION, {description.capitalize()}")
            
        else:
            print(f"Error: Unable to fetch data. Status Code:{response.status_code}")

    except requests.exceptions.RequestException as e:
            print(f"Connection Error: {e}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        
    except Exception as err:
        print(f"Unkown error occured: {err}")
        traceback.print_exc()
    



def get_forecasted_weather(city_name, num_days):

    query_parameters = {
            "key": weather_api_key,
            "q": city_name,
            "aqi": "no",
            "days": num_days
        }

    try:
        response = requests.get(url, query_parameters)

        if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)

            for forecast_day in weather_data["forecast"]["forecastday"]:
                day_date = forecast_day["date"]
                day_info = forecast_day["day"]

                max_temp = day_info["maxtemp_f"]
                min_temp = day_info["mintemp_f"]
                condition = day_info["condition"]["text"]
                avg_humidity = day_info["avghumidity"]

                print(f"\nDATE, {day_date}")
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
        traceback.print_exc()
        




if __name__ == "__main__":

# determine how/when to run either current ore forecasted
   
    # city_name query
    print("Returns T or F if KEY works", load_dotenv())


    city = input("Enter city name: ")
    days = int(input("Enter nubmer of days: "))

    get_current_weather(city)
    get_forecasted_weather(city, days)