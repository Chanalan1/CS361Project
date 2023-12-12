"""
HomePage.py

This script serves as the main interface for a weather application. It includes the main menu and handles user interactions to navigate different features of the app.
"""

import os
from Introduction import Intro
from AppWorks import Works
from GettingStarted import Started
from WeatherReport import Weather

def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Welcome:
    """
    The Welcome class manages the homepage display and user interactions.
    """

    @staticmethod
    def display_homepage():
        """
        Displays the homepage and handles user input to navigate to different parts of the application.
        """
        while True: 
            clear_terminal()
            print("-------------------- Weather APP Generator --------------------")
            print("   -------------------  Welcome Page  -------------------\n")
            print("1: Introduction to the app")
            print("2: How the app works")
            print("3: Getting Started/Help")
            print("4: Start Generating Weather Report")
            print("5: EXIT THE PROGRAM\n")
            print("---> Enter an integer (1-5) to choose an option <---")
            print("-----------------------------------------------------------------\n")
            
            try:
                answer = int(input("Welcome, what option would you like to get started with: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            if answer == 1:
                Intro.display_intro()
            elif answer == 2:
                Works.explanation()
            elif answer == 3:
                Started.rules()
            elif answer == 4:
                Weather.report()
            elif answer == 5:
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == '__main__':
    Welcome.display_homepage()
