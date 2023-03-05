from ast import While
from pickle import TRUE
import pymysql
from datetime import datetime
from time import sleep
import ProjectInnovation
import mysql.connector as connection
import pandas as pd
import logging
from sqlalchemy import false, true


conn = None

# MySQL connect to employees DB
def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    x = conn.cursor()
    logging.info('Connect to MySql')
    return x




# 4.4.1 1 (View Employees & Departments)
# The user is shown the list of Employee Names (in alphabetical order) and the Names of the
# Department each employee works in, in groups of 2:
def get_employ_dept():
    # a is required to set to zero for offset
    a = 0
    quit = ""
    while (quit != "q"):
        cursor = connect()
    
        query = """ Select e.name as employee, d.name as department
            from employee e
            JOIN dept d
            ON e.did = d.did
            ORDER by e.name
            LIMIT 2 OFFSET %s; """

        with conn:
            # logging query
            logging.info(query)

            cursor.execute(query, (a))
            employ_dept = cursor.fetchall()
            
            for x in employ_dept:
                print(x["employee"], "|", x["department"])
        # increase a by two to increase the offset for query
        a = a + 2
        
        # User can only input q to quit
        quit = input("-- Quit (q) --")
        logging.info('User input to quit ' + quit)
    conn.close
    logging.info('Close SQL connection for Choice 1')

# 4.4.2 2 (View Salary Details)
# The user is asked to enter an Employee ID:
def view_salary(number):
    print("\nSalary Details for Employee:" + number)
    print("------------------------------")
    cursor = connect()    
    query = """ Select format(min(salary),0) AS Minimum, format(avg(salary),0) AS Average, format(max(salary) ,2) AS Maximum
            from salary
            WHERE eid = %s; """

    with conn:

        logging.info(query)

        cursor.execute(query, number)
        Salaryresults = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(*field_names, sep="\t|\t")
        for value in Salaryresults:
            if value["Minimum"] == None:
                ProjectInnovation.countdown()
                logging.info('No employee number of ' + number)
                return
            else:
                print(value["Minimum"],"\t|\t" , value["Average"],"|\t" , value["Maximum"] )
    
    conn.close
    logging.info('Close SQL connection for Choice 2')
    ProjectInnovation.countdown()
    


# 4.4.3 3 (View by Month of Birth)
# The user is asked to enter a Month
# Function for SQL query to output results
# This function will only be called after user has input the correct month
# from view_MOB()
def qresults(intmonth):
        cursor = connect()    
        query = """ Select eid, name, DATE_FORMAT(dob, "%Y-%m-%d") as NewDate 
                from employee
                WHERE month(dob) = {}; """.format(intmonth)
        with conn:
            cursor.execute(query)
            logging.info(query)
            iresults = cursor.fetchall()
            for value in iresults:
                print(value["eid"],"|" , value["name"],"|" , value["NewDate"] )
        conn.close
        logging.info('Close SQL connection for Choice 3')
        ProjectInnovation.countdown()
        
                
# This function to detect user input 
def view_MOB():
    # Set mobresult to none
    mobresult = None    

    while mobresult is None:
        # Request Employee Number
        usermonth = input("Enter Month: ")
        logging.info('User input month ' + usermonth)

        try:
            if (usermonth.isnumeric() == True):
                intmonth = int(usermonth)
                logging.info('The user has input an integer ' + str(intmonth))
                if intmonth in range(1,13):
                    logging.info('The integer is the integer month of ' + str(intmonth))
                    # Function to run SQL query
                    qresults(intmonth)
                    mobresult = 1
                    logging.info('The user input the correct integer month set mobresult to ' + str(mobresult) + ' and exit')
                
            elif len(usermonth) == 3:
                try:
                    datetime_object = datetime.strptime(usermonth, "%b")
                    intmonth = datetime_object.month
                    # Function to run SQL query
                    qresults(intmonth)
                    mobresult = 2
                    logging.info('The user input the correct using the first 3 characters of the months name set mobresult to ' + str(mobresult) + ' and exit')
                except:
                    pass
        except:
            logging.info('The user has not input the required month ' + str(mobresult) + ' and start again')
            pass


# 4.4.4 4 (Add New Employee)
# The user is asked to enter an Employee ID, Name, and date of birth, as well as the ID of the
# department the employee will work in
def add_new_Emp(EID, NAME, DOB, DEPTID):
    # print("Part4")
    cursor = connect()

    query = "INSERT INTO employee VALUES (%s, %s, %s, %s)"

    try:
        logging.info(query)
        with conn:
            cursor.execute(query, (EID, NAME, DOB, DEPTID))

        conn.close
        logging.info('Close SQL connection for Choice 4')
        print("\nEmployee sucessfully added")
        
    except pymysql.err.IntegrityError as e:
        errors = str(e)
        if '1062' in errors:
            print("\n*** ERROR ***: " + EID + " already exists")
            logging.warning('1062 error: ' + str(e))
            sleep(2)
        elif '1452' in errors:
            print("\n*** ERROR ***: Department " + DEPTID + " does not exists")
            logging.warning('1452 error: ' + str(e))
            sleep(2)
        else:
            pass
    except pymysql.err.OperationalError as e:
        print("\n*** ERROR ***: Invalid DOB: " + DOB )
        logging.warning('Invalid DOB: ' + str(e))
        sleep(2)
    except Exception as e:
        logging.warning(str(e))
        pass
    ProjectInnovation.countdown()
   

    
# 4.4.5 5 (View Departments managed by Employee)
# The user is asked to enter an Employee ID. The Name and Budget of all departments managed by the
# employee with that ID are returned
def view_manage_dept(number):
    
    print("\nDepartments Managed by: " + number)
    print("------------------------------")
    cursor = connect()    
    query = """ Select  d.name as Department, d.budget as Budget
            from employee e
            JOIN dept d
            ON e.did = d.did
            WHERE eid = %s;"""

    with conn:
        logging.info(query + number)
        cursor.execute(query, number)
        mdresults = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(*field_names, sep="\t|\t")
        for value in mdresults:
            if value["Department"] == None:
                logging.info('The employee does not manage a department: ' + number)
                return
            else:
                print(value["Department"],"\t|\t" , value["Budget"], "\n")
    
    conn.close
    logging.info('Close SQL connection for Choice 5')
    ProjectInnovation.countdown()


# 4.4.6 6 (Add Manager to Department)
# The user is asked to enter an Employee ID and a Department ID.
# When both are entered, the Neo4j database is updated to show that that employee now manages
# that department
def view_Dept_Exists(DEPTID):
            
    cursor = connect()    
    query = """ Select did from dept
            WHERE did = %s; """

    with conn:
        logging.info(query)
        cursor.execute(query, DEPTID)
        deresults = cursor.fetchall()
        for value in deresults:
            if value["did"] == None:
                return false
            else:
                return true
    logging.info('Close SQL connection for Choice 6 view_Dept_Exists')
    conn.close


def view_Emplo_Exists(EID):
    
    cursor = connect()    
    query = """ Select eid from employee
            WHERE eid = %s; """

    with conn:
        logging.info(query)
        cursor.execute(query, EID)
        eeresults = cursor.fetchall()
        for value in eeresults:
            if value["eid"] == None:
                return false
            else:
                return true
    logging.info('Close SQL connection for Choice 6 def view_Emplo_Exists(EID):')
    conn.close


# 4.4.7 7 (View Departments)
# This option shows details of all Departments
def view_Dept():
        
    try:
        mydb = connection.connect(host="localhost", database = 'employees',user="root", passwd="root",use_pure=True)
        query = "Select * from dept;"
        logging.info(query)
        # save query to a pandas dataframe 
        result_dataFrame = pd.read_sql(query,mydb)
        mydb.close()
        logging.info('Close SQL connection for Choice 7')
        # return pandas dataframe
        return result_dataFrame
    except Exception as e:
        logging.warning(str(e))
        mydb.close()
        print("Error: ", e)
        
        
    
   









