import pymysql


def add_patient(ppsn, fName, surname, address, doctorID):
    db = pymysql.connect(host="localhost", user="root", password="root", db="hospital", cursorclass=pymysql.cursors.DictCursor)

    sql = "INSERT INTO patient_table VALUES  (%s, %s, %s, %s, %s)"

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, (ppsn, fName, surname, address, doctorID))
            db.commit()
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.InternalError as e:
            print(e)
        except Exception as e:
            print(e)
    

def find_patient(surname):
    db = pymysql.connect(host="localhost", user="root", password="root", db="hospital", cursorclass=pymysql.cursors.DictCursor)

    sql = """
            SELECT pt.ppsn, pt.first_name, pt.surname, dt.name
            from patient_table pt
            inner join doctor_table dt
                on pt.doctorID = dt.doctorID
            where surname like %s
        """

    with db:
        try:
            cursor = db.cursor()
            cursor.execute(sql, ("%" + surname + "%"))
            return cursor.fetchall()
            #db.commit()
        except pymysql.err.IntegrityError as e:
            print(e)
        except pymysql.err.InternalError as e:
            print(e)
        except Exception as e:
            print(e)
    
