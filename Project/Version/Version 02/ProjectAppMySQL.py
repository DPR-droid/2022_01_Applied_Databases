from ast import While
from pickle import TRUE
import pymysql
from datetime import datetime
from time import sleep
import ProjectInnovation
import ProjectAppNeo4j

from sqlalchemy import false, true


conn = None

# MySQL connect to employees DB
def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    x = conn.cursor()
    return x




# 4.4.1 1 (View Employees & Departments)
# The user is shown the list of Employee Names (in alphabetical order) and the Names of the
# Department each employee works in, in groups of 2:
def get_employ_dept():
    
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
            #print("First :" + str(a))
            cursor.execute(query, (a))
            employ_dept = cursor.fetchall()

            for x in employ_dept:
                print(x["employee"], "|", x["department"])
        a = a + 2
        # print("Repeat :" + str(a))
        quit = input("-- Quit (q) --")
    conn.close

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
        cursor.execute(query, number)
        Salaryresults = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(*field_names, sep="\t|\t")
        for value in Salaryresults:
            if value["Minimum"] == None:
                ProjectInnovation.countdown()
                return
            else:
                print(value["Minimum"],"\t|\t" , value["Average"],"|\t" , value["Maximum"] )
    
    conn.close
    ProjectInnovation.countdown()
    


# 4.4.3 3 (View by Month of Birth)
# The user is asked to enter a Month
def qresults(intmonth):
        cursor = connect()    
        query = """ Select eid, name, DATE_FORMAT(dob, "%Y-%m-%d") as NewDate 
                from employee
                WHERE month(dob) = {}; """.format(intmonth)
        with conn:
            cursor.execute(query)
            iresults = cursor.fetchall()
            # print(results)
            for value in iresults:
                print(value["eid"],"|" , value["name"],"|" , value["NewDate"] )
        conn.close
        ProjectInnovation.countdown()
        
                

def view_MOB():
    mobresult = None
    while mobresult is None:
        # Request Employee Number
        usermonth = input("Enter Month: ")
            # print(s)
        try:
            if (usermonth.isdigit() == True):
                intmonth = int(usermonth)
                # print(intmonth)
                if intmonth in range(1,13):
                    #print("Range: " + str(intmonth))
                    qresults(intmonth)
                    mobresult = 1
                
            elif len(usermonth) == 3:
                try:
                    datetime_object = datetime.strptime(usermonth, "%b")
                    intmonth = datetime_object.month
                    qresults(intmonth)
                    mobresult = 2
                except:
                    pass
        except:
            pass


# 4.4.4 4 (Add New Employee)
# The user is asked to enter an Employee ID, Name, and date of birth, as well as the ID of the
# department the employee will work in
def add_new_Emp(EID, NAME, DOB, DEPTID):
    # print("Part4")
    cursor = connect()

    query = "INSERT INTO employee VALUES (%s, %s, %s, %s)"

    #with conn:
    #    cursor.execute(query, (EID, NAME, DOB, DEPTID))
    #
    #    conn.close
    #    print("\nEmployee sucessfully added\n")
    #    sleep(2)
    try:
        with conn:
            cursor.execute(query, (EID, NAME, DOB, DEPTID))

        conn.close
        print("\nEmployee sucessfully added")
        sleep(2)
    except pymysql.err.IntegrityError as e:
        # print("Subject Error: ", e)
        errors = str(e)
        if '1062' in errors:
            print("\n*** ERROR ***: " + EID + " already exists\n\n")
        elif '1452' in errors:
            print("\n*** ERROR ***: Department " + DEPTID + " does not exists\n\n")
        else:
            pass
    except pymysql.err.OperationalError as e:
        print("\n*** ERROR ***: Invalid DOB: " + DOB )
    except Exception as e:
        # print("Error: ", e)
        pass
   

    
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
        cursor.execute(query, number)
        mdresults = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(*field_names, sep="\t|\t")
        for value in mdresults:
            if value["Department"] == None:
                return
            else:
                print(value["Department"],"\t|\t" , value["Budget"], "\n")
    
    conn.close
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
        cursor.execute(query, DEPTID)
        deresults = cursor.fetchall()
        for value in deresults:
            if value["did"] == None:
                return false
            else:
                #print(value["did"])
                return true
    
    conn.close


def view_Emplo_Exists(EID):
    # print("Yes this is here " + EID)

    cursor = connect()    
    query = """ Select eid from employee
            WHERE eid = %s; """

    with conn:
        cursor.execute(query, EID)
        eeresults = cursor.fetchall()
        for value in eeresults:
            if value["eid"] == None:
                return false
            else:
                # print(value["eid"])
                return true
    
    conn.close





   









