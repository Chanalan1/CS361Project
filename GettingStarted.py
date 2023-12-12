"""
Started.py

This module contains the Started class, which provides guidance for getting started with the Weather APP Generator. It includes instructions for navigating through the application's main menu.
"""


import os

def clear_terminal():
    """
    Clears the terminal
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Started:
    """
    Class that provides how to get started with the class
    """
    def rules():
        """
        Provides instructions on  how to navigate the app and reassures the user of any complications 
        """

        clear_terminal()
        print("-------------------- Weather APP Generator --------------------")
        print("   ------------------- Getting Started  -------------------")
        print()
        print("To get started with the application, return back to the welcome home page.")
        print("This can be done by hitting any key on your keyboard and navigate to the weather ")
        print("report section of the app by hitting the '4' key on your keyboard when prompted for")
        print("an option to choose from. Don't worry, if you want to return back to the homepage after ")
        print("maybe mistaking something, or you want to reread any of the instructions, you will have ")
        print("the option to do so. Please enjoy the application! ")
        print()
        print("-----------------------------------------------------------------")
        print()
        input("Press any key to go back to the main page!!! ")