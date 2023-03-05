import ProjectApp
from time import sleep

# https://www.geeksforgeeks.org/clear-screen-python/
# import only system from os
from os import system, name
  
# import sleep to show output for some time period
# define our clear function
def clear():
    # sleep(2)
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
    ProjectApp.display_menu()


# https://stackoverflow.com/questions/17220128/display-a-countdown-for-the-python-sleep-function
# Countdown function to Clear Data from screen
def countdown():
    print("\nClearing Data on Screen and Returning to Main Menu in:")
    for i in range(9,0,-1):
        print(f"{i}", end="\r", flush=True)
        sleep(1)
