def bhaskara_code(a, b, c):
    delta = (b**2) - 4*a*c
    x_1 = (-b + delta ** (1/2)) / (2*a)
    x_2 = (-b - delta ** (1/2)) / (2*a)
    
    print(f'O Valor de X1: ({x_1})')
    print(f'O Valor de X2: ({x_2})')



a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

bhaskara_code(a, b, c)