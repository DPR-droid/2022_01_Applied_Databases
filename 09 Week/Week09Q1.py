import Week09Q1DB




def main():
    display_menu()

    while True: 
        choice = input("Enter choice: ")


        if (choice == "1"):
            ppsn = input("PPSN: ")
            fName = input("fName: ")
            surname = input("surname: ")
            address = input("address: ")
            doctorID = input("doctorID: ")
            Week09Q1DB.add_patient(ppsn, fName, surname, address, doctorID)
            display_menu()
        elif (choice == "2"):
            surname = input("surname: ")
            patients = Week09Q1DB.find_patient(surname)
            for patient in patients:
                print(patient["ppsn"], "|", patient["first_name"], "|", patient["surname"], "|", patient["name"])
            
        else:
            break

def display_menu():
    print("")
    print("Menu")
    print("=====")
    print("1 - Add patient")
    print("2 - Find patient")
    print("x - Exit")


if __name__ == "__main__":
    main()