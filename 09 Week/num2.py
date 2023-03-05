import num2DB
import pymysql

def get_number():
    return input("Enter Number: ")

def main():
    name = input("Enter Subject: ")
    teacher = input("Enter teacher: ")
    lc = input("Enter on Leaving Cert 1/0: ")

    try:
        num2DB.add_subject(name, teacher, lc)
    except pymysql.err.ProgrammingError as e:
        print("Programming Error: ", e)
    except pymysql.err.IntegrityError as e:
        print("Subject Error: ", e)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()