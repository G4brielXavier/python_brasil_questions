salario = float(input("Seu Salario: "))

inss = salario * 0.11
ir = salario * 0.8
sindicato = salario * 0.5
salario_liquido = salario - (0.11 + 0.8 + 0.5)

print(f'Salario Bruto: R${salario}')
print(f'INSS: R${inss}')
print(f'IR: R${ir}')
print(f'Salario Liquido: R${salario_liquido}')


