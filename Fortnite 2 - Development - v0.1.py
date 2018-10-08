import time
import os
#-------------------------------------------------------------------------------
# Name:        Fortnite 2
# Purpose:  Creating the best new game, with AAA development.
#
# Author:      Sam
#
# Created:     19/09/2018
#-------------------------------------------------------------------------------



playerName = input("What is your player name? ")

health = 100


print("""
Welcome,""", playerName ,"""to Fortnite 2!

Make sure to default dance on the haters!""")

#Define this and use it as a function for else if none of the options are selected when the user inputs
def runMenu():
    mainMenu = input("""Main Menu:
Solo
Duos
Squad
Settings
Skins

Type in the one you want to use: """)

if mainMenu == "Solo":
    print("Selected solo!")
    time.sleep(2)
    os.system('cls')
    print("Fortnite 2 is loading.")
    time.sleep(2)
    os.system('cls')
    print("Fornite 2 is loading..")
    time.sleep(2)
    os.system('cls')
    print("Fortnite 2 is loading...")
    time.sleep(2)
    os.system('cls')
#thankBattleBus = input("Do you want to thank the battle bus driver? Y/N")
#if thankBattleBus == "Y":
#Code to be fixed later innit


elif mainMenu == "Duos":
    print("Cannot run right now")
elif mainMenu == "Squad":
    print("Cannot run right now")
elif mainMenu == "Skins":
    print("Thanos dududududududu Thanos dududududududuudud Thanos dududududududu")
elif mainMenu == "Settings":
    input("""Settings:


""")
else:
    runMenu()
