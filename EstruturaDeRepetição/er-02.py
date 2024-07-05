name = input("Name: ")

def registred():
    print("Registro concluído")

def set_password(name):
    password = input("Password: ")
    if not password == name:
        registred()
    elif password == name or password == "":
        set_password(name)
        
set_password(name)