shift = input("[M/A/N]: ").upper()

if shift in ["M", "A", "N"]:
    if shift == "M":
        print("Good Morning")
    elif shift == "A":
        print("Good Afternoon")
    elif shift == "N":
        print("Good Night")
else:
    print("unknown value :[")