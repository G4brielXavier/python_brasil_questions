genero = input("[H/M]: ").upper()
altura = float(input("Altura: "))

if genero in ["H", "M"]:
    if genero == "H":
        peso = (72.7 * altura) - 58
    elif genero == "M":
        peso = (62.1 * altura) - 44.7

print(f'Seu Peso: {str(peso):.1f}')