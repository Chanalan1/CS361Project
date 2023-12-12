"""
AppWorks.py

This module contains the Works class, which provides an explanation of how the Weather APP Generator works. It includes details about the APIs used in the application for fetching weather data.
"""

import os

def clear_terminal():
    """
    Clears the terminal screen. Uses different commands based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Works:
    """
    The Works class provides a detailed explanation of how the weather application operates, particularly focusing on the use of weather APIs.
    """

    @staticmethod
    def explanation():
        """
        Displays information about the weather APIs used in the application and how the app functions.
        """
        clear_terminal()
        print("-------------------- Weather APP Generator --------------------")
        print("   ------------------- App Explanation  -------------------\n")
        print("The App works by leveraging APIs such as weatherapi and weatherstack, which provide comprehensive weather data.\n")
        
        # Explanation of weatherapi
        print("Weatherapi API:")
        print("Weatherapi allows access to a variety of weather data including current conditions, ")
        print("hourly forecasts for up to 4 days, and climatic forecasts for up to 30 days. ")
        print("It is an essential tool for obtaining real-time weather analytics and creating future weather trends. \n")
        
        # Explanation of weatherstack API
        print("Weatherstack API:")
        print("Weatherstack API offers real-time weather information and historical data. ")
        print("It provides detailed weather reports including temperature, wind speed, humidity, ")
        print("UV index, and more. It's ideal for applications requiring reliable and accurate weather information. \n")
        
        print("Using these APIs, this app allows users to customize their weather reports. ")
        print("For example, users can obtain specific data like humidity and temperature for a chosen city. ")
        print("The customization feature ensures that the report includes only the necessary information, ")
        print("avoiding unnecessary data clutter.")
        print("-----------------------------------------------------------------\n")
        input("Press any key to go back to the main page!!! ")