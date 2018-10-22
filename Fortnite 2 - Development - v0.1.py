import time
import os

playerName = input("What is your player name? ")

health = 100


print("""
Welcome,""", playerName ,"""to Fortnite 2!
Make sure to default dance on the haters!""")


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
        input("Do you want to thank the battle bus driver? Y/N: ")
        if input == "Y":
            print("Thanks battle bus driver")
        else:
            print("Wowie aren't you nice")



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
runMenu()
