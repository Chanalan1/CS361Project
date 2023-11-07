import os

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


class Works:

    def explanation():

        clear_terminal()
        print("-------------------- Weather APP Generator --------------------")
        print("   ------------------- App Explanation  -------------------")
        print()
        print("The App works by leveraging the weatherapi API that is available using python. ")
        print("Weatherapi allows users to call features such as current weather data, hourly forecast for 4 days, ")
        print("climatic forecast for 30 days and other import features related to the weather. ")
        print()
        print("This app will allow you to customize the weather information you want, for example the humidty ")
        print("and temperature for the city Seattle, and give you that data for you to use. The customization allows ")
        print("a user to only have what they want to know on that report, so that information not needed does not ")
        print("show.")
        print("-----------------------------------------------------------------")
        print()
        input("Press any key to go back to the main page!!! ")