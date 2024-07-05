letter = input("type it a letter: ")

if letter in ["a", "e", "i", "o", "u"]:
    print(f'"{letter}" is a vogal')
else:
    print(f'"{letter}" is a consoant')