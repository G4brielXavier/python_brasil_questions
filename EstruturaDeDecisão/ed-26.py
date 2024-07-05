# alcool
# <= 20L - 3% por litro
# > 20L - 5% por litro 

# gasolina
# <= 20L - 4% por litro
# > 20L - 6% por litro

liters_solds = float(input("Liters: "))
type_liquid = input("[A/G]: ").upper()

liter_gas = 2.5
liter_al = 1.9

price = 0

if type_liquid in ["A", "G"]:
    if type_liquid == "A":
        print("Tipo de Substância: Álcool")
        if liters_solds <= 20:
            price = (liters_solds * liter_al) * 0.3
        elif liters_solds > 20:
            price = (liters_solds * liter_al) * 0.5
    elif type_liquid == "G":
        print("Tipo de Substância: Gasolina")
        if liters_solds <= 20:
            price = (liters_solds * liter_gas) * 0.4
        elif liters_solds > 20:
            price = (liters_solds * liter_gas) * 0.6

print(f'Preço: R${price:.2f}')