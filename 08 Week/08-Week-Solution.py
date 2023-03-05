


def doubleNumber(x):
    return x * 2

def main():
    arrayNum = [1,2,7,9]
    arrayNum2 = []
    for x in arrayNum:
        
        arrayNum2.append(doubleNumber(x))

    print(arrayNum2)
    

if __name__ == "__main__":
	# execute only if run as a script 
	main()