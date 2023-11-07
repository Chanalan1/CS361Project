import os

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Intro:
    
    def display_intro():
        clear_terminal()
        print()
        print("-------------------- Weather APP Generator --------------------")
        print("   -------------------  Introduction  -------------------")
        print()
        print("This application works by generating a weather report for the user. The weather ")
        print("report can be used by local weather stations, enthusiasts, or for those that want ")
        print("real-time analytics of current weather and to create future weather trends. ")
        print()
        print("For those wondering what a weather report is, they are made up of components that tell us ")
        print("the conditions of our area. To put it simply, it is a systematic statement of the existing and usually ")
        print("the predicted meteorological conditions over a particular area.")
        print("-----------------------------------------------------------------")
        print()
        input("Press any key to go back to the main page!!! ")

