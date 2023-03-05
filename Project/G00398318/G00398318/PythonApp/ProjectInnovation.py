from sqlalchemy import false, true
import ProjectApp
from time import sleep
import os
from os import system, name
import logging

# https://www.geeksforgeeks.org/clear-screen-python/
# import only system from os  
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
    logging.info('clear screen')
    ProjectApp.display_menu()


# https://stackoverflow.com/questions/17220128/display-a-countdown-for-the-python-sleep-function
# Countdown function to Clear Data from screen
# and return to main menu
def countdown():
    print("\nClearing Data on Screen and go to Main Menu in:")
    for i in range(9,0,-1):
        # print number to screen then remove 
        print(f"{i}", end="\r", flush=True)
        # pause program for 1 second
        sleep(1)
        logging.info('countdown')



# Function to check if all files required for the app are present in the same folder
# Assist in debugging for the app 
def app_checker():
    # List of Files
    appfiles = ["ProjectAppMySQL.py", "ProjectInnovation.py", "ProjectAppNeo4j.py", "ProjectApp.py"]
    #appfiles = ["ProjectAppMySQL.py", "ProjectInnovation.py", "ProjectAppNeo4j.py", "ProjectApp1.py"]
    # Get currrent working directory
    filelocation = os.path.dirname(__file__)
    # Use list of file to check if that they are present
    for file in appfiles:
        try:
            # try open file using path and filename
            # output to screen 
            with open(filelocation + "\\" + file) as f:
                #print("\nProject Apps File Found")
                #print(file)
                logging.info('Application ' + file)
        except IOError as e:
            # Error if files not found outpur missing file name
            logging.warning('Application ' + file)
            logging.warning(e)
            print("\nProject Apps File Not Found " + file)
            exit()
            #return false
    return true
