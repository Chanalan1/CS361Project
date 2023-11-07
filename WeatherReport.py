import os
import requests

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Weather:

    API_KEY = 'b20047520e8450be222eb7a159004e53'
    BASE_URL = 'http://api.weatherstack.com/current'  # Base URL for current weather
    
    @staticmethod
    def report():
        clear_terminal()
        print("-------------------- Weather APP Generator --------------------")
        print("   ----------------- Generate your report  -----------------")
        print("Below you may generate your customized weather report or you may ")
        print("use our 'quick' generator that will ask you for a city and return the temp and humidity for that city")
        print()
        print("The following customizations are available: ")
        print("---------------------------------------------------------------------------------------------------")
        print("Wind Speed: wind_speed, Wind Degree: wind_degree, Wind Direction: wind_dir")
        print("Pressure: pressure, Precipitation: precipitation, Humidity: humidity")
        print("Cloud Cover: cloudcover, UV Index: uv_index, Visibility: visibility")
        print("---------------------------------------------------------------------------------------------------")

        checker = True

        while checker:
            
            print()
            answer = input("Press 1 if you want to generate a quick report, press 2 if you want to make a customized report, press 3 to exit: ")

            if answer == "1":
                print("Micro Service still being worked on")

            elif answer == "2":
                city = input("Enter the city name for the weather report: ")
                print()
                params_list = input("Enter the parameters you want (e.g., temperature,humidity,wind_speed **remember to use commas**): ")
                print()
                params_list = params_list.replace(' ', '').split(',')  # Remove any spaces and split by comma
                
                params = {
                    'access_key': Weather.API_KEY,
                    'query': city,
                    'units': 'f'  # defaults to Fahrenheit
                }
                response = requests.get(Weather.BASE_URL, params=params)
                weather_data = response.json()

                if 'current' in weather_data:
                    print(f"Weather Report for {city}:")
                    for param in params_list:
                        if param in weather_data['current']:
                            print(f"{param.capitalize()}: {weather_data['current'][param]}")
                        else:
                            print(f"{param.capitalize()}: Not available")
                else:
                    error_message = weather_data.get('error', {}).get('info', "An error occurred.")
                    print(error_message)

            elif answer == "3":
                checker = False

# To use the Weather class
if __name__ == "__main__":
    Weather.report()