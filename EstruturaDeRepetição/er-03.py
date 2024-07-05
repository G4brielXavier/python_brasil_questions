def insertName():
    name = input("Seu nome: ")
    if not name == "" and len(name) > 3:
        return name
    else:
        print("")
        print("Seu nome precisa ter mais de 3 caracteres e não pode deixar em branco.")
        print("")
        insertName()

def insertAge():
    age = int(input("Sua idade: "))
    if age > 0 and age <= 150:
        return age
    else:
        print("")
        print("Sua idade precisa estar entre 0 e 150.")
        print("")
        insertAge()
      
def insertWage():
    wage = float(input("Seu salário: "))
    if wage > 0:
        return wage 
    else:
        print("")
        print("Não pode ser vazio ou 0.")
        print("")
        insertWage()
        
def insertGenrer():
    genrer = input("[F/M]: ").lower()
    if genrer in ['f', 'm']:
        return genrer
    else:
        print("")
        print("Somente F para Feminino e M para Masculino.")
        print("")
        insertGenrer()
        
def insertState():
    state = input("[S/C/V/D]: ").lower()
    if state in ['s', 'c', 'v', 'd']:
        return state
    else:
        print("")
        print("S = Solteiro \n C = Casado \n V = Viúvo(a) \n D = Divorciado.")
        print("")
        insertState()
    

      
name = insertName()      
age = insertAge()
wage = insertWage()
genrer = insertGenrer()
state = insertState()

print("Registro Concluído!")
            