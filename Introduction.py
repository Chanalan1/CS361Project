"""
Intro.py

This module contains the Intro class, which is responsible for displaying the introduction of the Weather APP Generator. The introduction explains the purpose and functionality of the application.
"""

import os

def clear_terminal():
    """
    Clears the terminal screen. Uses different commands based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Intro:
    """
    The Intro class handles the display of the introductory section of the weather application.
    """

    @staticmethod
    def display_intro():
        """
        Displays the introduction of the weather app to the user.
        """
        clear_terminal()
        print("\n-------------------- Weather APP Generator --------------------")
        print("   -------------------  Introduction  -------------------\n")
        print("This application works by generating a weather report for the user. The weather ")
        print("report can be used by local weather stations, enthusiasts, or for those that want ")
        print("real-time analytics of current weather and to create future weather trends. \n")
        print("For those wondering what a weather report is, they are made up of components that tell us ")
        print("the conditions of our area. To put it simply, it is a systematic statement of the existing and usually ")
        print("the predicted meteorological conditions over a particular area.")
        print("-----------------------------------------------------------------\n")
        input("Press any key to go back to the main page!!! ")

