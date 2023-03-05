
# Main function
from ast import Num
from numpy import array


def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			array = fill_array()
			display_menu()
		elif (choice == "2"):
			print(array)
			display_menu()
		elif (choice == "3"):
			find_gt_in_array(array)
			display_menu()
		elif (choice == "4"):
			break;
		else:
			display_menu()
			
			
def fill_array():
# Write the necessary code to fill the array.
# -1 should not be part of the array
    array = []
    while True:
        x = int(input("Enter number: "))
        if (x == -1):
            break
        array.append(x)
    return array


def find_gt_in_array(array):
# Write the necessary code to get a number from the user
# and print out all numbers in the array that are greater
# than this number
    number = int(input("Enter number: "))
    for x in array:
        if (x > number):
            print(x)



def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()
