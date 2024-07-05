def validation():
    n = int(input("Number: "))
    if n <= 10 and n > 0:
        return n
    else:
        validation()
        
number = validation()

