"""
WeatherReport.py

This file contains all the methods and classes needed to generate both a quick weather report and a more detailed report
that leverages the 2 API's Weatherstack and Weatherapi.
"""


import os
import requests
import zmq
import json


def clear_terminal():
    """
    Clears out the terminal after a task has been finished
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Weather:

    """
    Weather class that contains the methods needed to generate a quick report and detailed report.
    
    For the quick report, it uses zmq to send a request to the microservice, wait for a response and use the response for the report.

    For the detailed report, it uses the API and ask the user for input parameters to generate their own detailed report.
    """

    API_KEY = 'b20047520e8450be222eb7a159004e53'
    BASE_URL = 'http://api.weatherstack.com/current'  # Base URL for current weather


    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:5556")

    def send_request(self, function, parameters):
        # Send the function request
        self.socket.send_json(json.dumps({'function': function}))
        # Send the parameters as a separate message
        self.socket.send_json(parameters)  # No need to dump, as it's already a JSON string
        # Receive the response
        return self.socket.recv_json()

    
    @staticmethod
    def report():
        """
        The prompt screeen that explains the steps needed to generate the report as well as input suggestions
        
        """
        weather = Weather()
        clear_terminal()
        print("-------------------- Weather APP Generator --------------------")
        print("   ----------------- Generate your report  -----------------")
        print()
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
                city = input("What city would you like to generate a forecast for?: ")
                parameters = json.dumps({'cityName': city})
                forecast_data = weather.send_request('forecast', parameters)
        
                print(f"Forecast Report for {city}:")
                for entry in forecast_data.get('list', []):
            # Extracting the date and time
                    date_time = entry.get('dt_txt')
            # Extracting the main weather parameters
                    temp = entry.get('main', {}).get('temp')
            # Extracting the weather condition
                    condition = entry.get('weather', [{}])[0].get('description')
                    print(f"Date: {date_time}, Temperature: {temp}°F, Conditions: {condition}")


            elif answer == "2":
                while True:  # This loop will keep running until the user confirms or chooses to exit
                    city = input("Enter the city name for the weather report: ")
                    print()
                    params_list = input("Enter the parameters you want (e.g., temperature,humidity,wind_speed **remember to use commas**): ")
                    print()
                    # Confirmation prompt
                    confirm = input("You have entered the city as '" + city + "' and parameters as '" + ','.join(params_list) + "'. Are you sure? (yes/no): ")
                    if confirm.lower() == 'yes':
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
                        break  # Exit the loop after generating the report
                    elif confirm.lower() == 'no':
                        # If the user enters 'no', the loop will start over, prompting for city and parameters again
                        print("Let's try entering the city and parameters again.")
                    else:
                        print("Please enter 'yes' or 'no'.")

            elif answer == "3":
                checker = False

# To use the Weather class
if __name__ == "__main__":
    Weather.report()