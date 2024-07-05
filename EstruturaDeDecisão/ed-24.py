def par_impar(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 1:
        print(f'{n1} é par | {n2} é ímpar')
    elif n1 % 2 == 1 and n2 % 2 == 0:
        print(f'{n1} é ímpar | {n2} é par')
    elif n1 % 2 == 0 and n2 % 2 == 0:
        print(f'{n1} é par | {n2} é par')
    elif n1 % 2 == 1 and n2 % 2 == 1:
        print(f'{n1} é ímpar | {n2} é ímpar')

def pos_neg(n1, n2):
    if n1 < 0 and n2 >= 0:
        print(f'{n1} é negativo | {n2} é positivo')
    elif n1 >= 0 and n2 < 0:
        print(f'{n1} é positivo | {n2} é negativo')
    elif n1 >= 0 and n2 >= 0:
        print(f'{n1} é positivo | {n2} é positivo')
    elif n1 < 0 and n2 < 0:
        print(f'{n1} é negativo | {n2} é negativo')

def int_float(n1, n2):
    if isinstance(n1, int) and isinstance(n2, float):
        print(f'{n1} é inteiro | {n2} é decimal')
    elif isinstance(n1, float) and isinstance(n2, int):
        print(f'{n1} é decimal | {n2} é inteiro')
    elif isinstance(n1, int) and isinstance(n2, int):
        print(f'{n1} é inteiro | {n2} é inteiro')
    elif isinstance(n1, float) and isinstance(n2, float):
        print(f'{n1} é decimal | {n2} é decimal')

n1 = float(input("n1: "))
n2 = float(input("n2: "))

option = input("[ a : par ou impar | b : positivo ou negativo | c : inteiro ou decimal ]: ")

if option in ["a", "b", "c"]:
    if option == "a":
        par_impar(n1, n2)
    elif option == "b":
        pos_neg(n1, n2)
    elif option == "c":
        int_float(n1, n2)