genrer = input("[M/W]: ").upper()

if genrer in ["M", "W"]:
    if genrer == "M":
        print(f'{genrer} is man')
    elif genrer == "W":
        print(f'{genrer} is woman')
else:
    print("Genrer Invalid!")