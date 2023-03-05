import pymysql

"""Error Code: 1064. You have an error in your SQL syntax; 
check the manual that corresponds to your MySQL server version for the right syntax to use near 'select * from salaries' at line 4
"""

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost", user="root", password="root", db="school", cursorclass=pymysql.cursors.DictCursor)


def add_subject(n, t, lc):
    if (not conn):
        connect()

    query = "INSERT INTO subject VALUES (%s, %s, %s)"

    with conn:
        cursor = conn.cursor()
        x = cursor.execute(query, (n, t, lc))
        print(x)
    