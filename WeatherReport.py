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
        # ... [rest of the intro text]

        checker = True

        while checker:
            print()
            answer = input("Press 1 if you want to generate a quick report, press 2 if you want to make a customized report, press 3 to exit: ")

            if answer == "1":
                print("Micro Service still being worked on")

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