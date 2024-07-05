from tabulate import tabulate

carnes = ["Filé Duplo", "Alcatra", "Picanha"]

print(f'Carnes: {carnes}')
tipo_de_carne = input("Qual o tipo de carne?: ").lower()
qty_de_carne = int(input("Quantidade: "))
card_super = input("Cartão Super? [s/n]: ")



def calc(carne, qty, card):
    price = 0
    
    if carne == "filé duplo":
        if qty <= 5:
            if card == "s":
                price = (qty * 4.9) * 0.5
            else:
                price = qty * 4.9
        elif qty > 5:
            if card == "s":
                price = (qty * 5.8) * 0.5
            else:
                price = qty * 5.8
    elif carne == "alcatra":
        if qty <= 5:
            if card == "s":
                price = (qty * 5.9) * 0.5
            else:
                price = qty * 5.9
        elif qty > 5:
            if card == "s":
                price = (qty * 6.8) * 0.5
            else:
                price = qty * 6.8
    elif carne == "picanha":
        if qty <= 5:
            if card == "s":
                price = (qty * 6.9) * 0.5
            else:
                price = qty * 6.9
        elif qty > 5:
            if card == "s":
                price = (qty * 7.8) * 0.5
            else:
                price = qty * 7.8
                
    return price
        


price_total = calc(tipo_de_carne, qty_de_carne, card_super)

print(" ")
print(" ")
print("---------- -Super- ----------")
print(f'Tipo: {tipo_de_carne.capitalize()}')
print(f'Quantidade: {qty_de_carne}')
print(f'Com Super Card?: {card_super}')
print(f'Valor á pagar: R${price_total}')