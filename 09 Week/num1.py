import num1DB

def get_number():
    return input("Enter Number: ")

def main():
    while True: 
        try:
            number = int(get_number())
            teachers = num1DB.get_experience(number)
            for teacher in teachers:
                print(teacher["tid"], "|", teacher["Name"], "|", teacher["level"], "|", teacher["experience"], "|", teacher["dob"])
            break
        except Exception as e:
            print("Invalid number, try again")


if __name__ == "__main__":
    main()