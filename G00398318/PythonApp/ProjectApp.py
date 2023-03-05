# https://docs.python.org/3/library/logging.html
# logging data to a text file
import logging
logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p',
                    filename = 'ProjectApp.log',
                    level=logging.DEBUG) 

# Imports
from sqlalchemy import false, true
# Possible fix to "NameError: name 'open' is not defined" 
# when logging really late during the Python finalization
import aiohttp

# Import Python Programs
import ProjectAppMySQL
import ProjectInnovation
import ProjectAppNeo4j


# main 
def main():
    # Function found in ProjectInnovation.py to debug if python programs are available
    ProjectInnovation.app_checker()
    logging.info('All apps found')
   
    # Function found in ProjectInnovation.py to countdown then clear screen and go to menu
    ProjectInnovation.countdown()    
    # display_menu()
    logging.info('Main Program complete')
    print('')
    menu()
    

# Main
def menu():
    # memory7 used for 7 - View Departments of user choice
    # memory7 is set to 1 
    memory7 = 1

    # Function found in ProjectInnovation.py to countdown then clear screen and go to menu
    ProjectInnovation.clear()

    while True: 
        choice = input("Choice: ")
        # 4.4.1 1 (View Employees & Departments)
        if (choice == "1"):
            logging.info('user Select: 1 - View Employees & Department')
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.get_employ_dept()

            # Return to display menu for user
            ProjectInnovation.clear()
            
        # 4.4.2 2 (View Salary Details)
        elif (choice == "2"):
            # Request Employee Number
            logging.info('user Select: 2 - View Salary Details')
            number = input("\nEnter EID: ")
            
            logging.info('Enter EID: ' + number)
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_salary(number)
            
            # Return to display menu for user
            ProjectInnovation.clear()
        
        # 4.4.3 3 (View by Month of Birth)
        elif (choice == "3"): 
            logging.info('user Select: 3 - View by Month of Birth')
            print("\n")
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_MOB()

            # Return to display menu for user
            ProjectInnovation.clear()

        # 4.4.4 4 (Add New Employee)
        elif (choice == "4"): 
            logging.info('user Select: 4 - Add New Employee')
            print("\nAdd New Employee")
            print("------------------")
            # Requireed input from user
            EID = input("EID: ")
            NAME = input("NAME: ")
            DOB = input("DOB: ")
            DEPTID = input("Dept ID: ")

            logging.info('User input:' + EID + ' ' + NAME + ' ' + DOB + ' ' + DEPTID)
            # Function located in ProjectAppMySQL.py3
            ProjectAppMySQL.add_new_Emp(EID, NAME, DOB, DEPTID)

            # Return to display menu for user
            ProjectInnovation.clear()
            
        # 4.4.5 5 (View Departments managed by Employee)
        elif (choice == "5"): 
            logging.info('user Select: 5 - View Department managed by Employee')
            number = input("Enter EID: ")
            logging.info('User input:' + number)
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_manage_dept(number)

            # Return to display menu for user
            ProjectInnovation.clear()
            
        # 4.4.6 6 (Add Manager to Department)
        elif (choice == "6"): 
            logging.info('user Select: 6 - Add Manager to Department')
            check = ""
            while check != 1:
                EID = input("\nEnter EID: ")
                DEPTID = input("Enter DID: ")
                logging.info('User input:' + EID + ' ' + DEPTID)
                # Function located in ProjectAppNeo4j.py
                manaNeo = ProjectAppNeo4j.get_Neo_Results(DEPTID)
                if manaNeo == true:
                    pass
                else:
                    print("\nDepartment " + DEPTID + " is already managed by " + manaNeo + "\n")
                    logging.info("Department " + DEPTID + " is already managed by " + str(manaNeo))
                    ProjectInnovation.countdown()
                    # check is equal to 1 exit while loop
                    check = 1
                logging.info("Result of manaNeo " + str(manaNeo))
                
                # ProjectInnovation.clear()
                # Function located in ProjectAppMySQL.py
                dept_e = ProjectAppMySQL.view_Dept_Exists(DEPTID)
                # print("view_Dept_Exists " + str(dept_e))
                if dept_e == None:
                    logging.info("Department " + DEPTID + " does not exist")
                    print("Department " + DEPTID + " does not exist")
                logging.info("view_Dept_Exists " + str(dept_e))

                # Function located in ProjectAppMySQL.py
                emply_e = ProjectAppMySQL.view_Emplo_Exists(EID)
                # print("view_Emplo_Exists " + str(emply_e))
                if emply_e == None:
                    logging.info("Department " + EID + " does not exist")
                    print("Department " + EID + " does not exist")
                logging.info("view_Emplo_Exists " + str(emply_e))


                # all functions must return true to be succesful.
                if manaNeo == true and dept_e == true  and emply_e == true :
                    # check is equal to 1 exit while loop
                    check = 1
                    ProjectAppNeo4j.add_manages(EID, DEPTID)
                    print("\nEmployee: ", EID, "now manages Department", DEPTID)
                    ProjectInnovation.countdown()
                    logging.info("Add Manager to Department is sucessful")
            # Return to display menu for user
            ProjectInnovation.clear()
            
        # 4.4.7 7 (View Departments)
        elif (choice == "7"):
            logging.info('user Select: 7 - View Departments')
            # memory7 used for choice 7
            # memory7 is set to 1 at beginning of menu
            # When the user first selects choice 7 it runs the query
            if memory7 == 1:
                output = ProjectAppMySQL.view_Dept()
                print("\n")
                print(output.to_string(index=False))
                # When choice 7 is selected memory7 is changed to 7
                # and will not recall the query
                logging.info("Query Sql for list of deparments in choice 7")
                memory7 = 7
                ProjectInnovation.countdown()
            else:
                logging.info("Your memory has inceased by a factor of " + str(memory7))
                print("\n")
                print(output.to_string(index=False))
                print("\n")
                ProjectInnovation.countdown()
            ProjectInnovation.clear()
            

        elif (choice == "x"):
            logging.info("Exit Python Program")
            # Assist with finalisation and exit logging without errors
            logging.shutdown()
            #sys.is_finalizing()
            break
        
        else:
            # If user does not choose the correct input
            # Print a message to the screen 
            # Returns user to main menu 
            print("\n***Please choose a number from above list or to exit press x***\n")
            logging.info("User input error " + choice)
            ProjectInnovation.countdown()
            ProjectInnovation.clear()

# Displays a main menu for User
def display_menu():
    logging.info('display_menu')
    print("Employees\n---------\n")
    print("Menu")
    print("=====")
    print("1 - View Employees & Department")
    print("2 - View Salary Details")
    print("3 - View by Month of Birth")
    print("4 - Add New Employee")
    print("5 - View Department managed by Employee")
    print("6 - Add Manager to Department")
    print("7 - View Departments")
    print("x - Exit application")


if __name__ == "__main__":
    main()