peso_peixe = int(input("Peso do peixe: "))
excesso = 50
multa_valor = 4

peso_excedente = 0
multa = 0

if peso_peixe < excesso:
    print("Sem multa.")
elif peso_peixe >= excesso:
    peso_excedente = peso_peixe - excesso
    multa = multa_valor * peso_excedente
    
    print(f'Peso Excedente: {str(peso_excedente)}Kg')
    print(f'Multa á pagar: R${str(multa)}')
