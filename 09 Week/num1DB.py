import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="school", cursorclass=pymysql.cursors.DictCursor)


def get_experience(number):
    if (not conn):
        print("No connection")
        connect()
    else:
        print("Already connected")

    query = "Select * FROM teacher WHERE experience < %s"

    with conn:
        cursor = conn.cursor()
        cursor.execute(query, (number))
        x = cursor.fetchall()
        return x
    
    #print("in function", number)