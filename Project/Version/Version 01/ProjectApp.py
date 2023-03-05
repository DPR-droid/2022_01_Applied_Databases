import ProjectAppMySQL
import ProjectInnovation
from time import sleep
import pymysql



# Main
def main():
    ProjectInnovation.clear()

    while True: 
        choice = input("Choice: ")
        # 4.4.1 1 (View Employees & Departments)
        if (choice == "1"):

            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.get_employ_dept()

            # Return to display menu for user
            ProjectInnovation.clear()
            
        # 4.4.2 2 (View Salary Details)
        elif (choice == "2"):
            # Request Employee Number
            number = input("\nEnter EID: ")
            
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_salary(number)
            
            # Return to display menu for user
            ProjectInnovation.clear()
        
        # 4.4.3 3 (View by Month of Birth)
        elif (choice == "3"): 

            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_MOB()

            # Return to display menu for user
            ProjectInnovation.clear()

        # 4.4.4 4 (Add New Employee)
        elif (choice == "4"): 
            
            EID = input("EID: ")
            NAME = input("NAME: ")
            DOB = input("DOB: ")
            DEPTID = input("Dept ID: ")

            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.add_new_Emp(EID, NAME, DOB, DEPTID)

            # Return to display menu for user
            # ProjectInnovation.clear()
            display_menu()
            
        # 4.4.5 5 (View Departments managed by Employee)
        elif (choice == "5"): 

            number = input("Enter EID: ")
            # Function located in ProjectAppMySQL.py
            ProjectAppMySQL.view_manage_dept(number)

            # Return to display menu for user
            # ProjectInnovation.clear()
            display_menu()
            


        elif (choice == "x"):
            break
        
        else:
            # If user does not choose the correct input
            # Print a message to the screen 
            # Sleeps
            # Returns user to main menu 
            print("\n\n***Please choose a number from above list or to exit press x***\n\n")
            sleep(1)
            display_menu()

# Displays a main menu for User
def display_menu():
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