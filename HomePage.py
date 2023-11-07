import os
from Introduction import Intro
from AppWorks import Works
from GettingStarted import Started
from WeatherReport import Weather
def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Welcome:
    
    def homepage():
        # start the homepage loop
        while True: 
            clear_terminal()
            print("-------------------- Weather APP Generator --------------------")
            print("   -------------------  Welcome Page  -------------------")
            print()
            print("1: Introduction to the app ")
            print("2: How the app works ")
            print("3: Getting Started/Help ")
            print("4: Start Generating Weather Report ")
            print("5: EXIT THE PROGRAM ")
            print()
            print()
            print("---> Please make sure that you are entering an integer in the range of option 1 - 5! <---")
            print("-----------------------------------------------------------------")
            print()
            answer = input("Welcome, what option would you like to get started with: ")

            if answer == "1":
                Intro.display_intro()
            elif answer == "2":
                Works.explanation()
            elif answer == "3":
                Started.rules()
            elif answer =="4":
                Weather.report()
            elif answer == "5":
                return False  
            


# Call the homepage to start the application
if __name__ == '__main__':
    Welcome.homepage()
