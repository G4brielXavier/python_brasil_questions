largura = float(input("Largura: "))
altura = float(input("Altura: "))

metros_quadrados = largura * altura
litros_de_tinta = metros_quadrados / 6

capacidade_latas = 5
capacidade_galoes = 10

escolha = str(input("[G/L]: ").upper())

if escolha == "G":
    
    if litros_de_tinta > 10:
        latas_de_tinta = litros_de_tinta / capacidade_galoes
        valor_da_lata = 80 * latas_de_tinta
        print(f'Metros Quadrados: {metros_quadrados}m²')
        print(f'Litros de Tinta: {litros_de_tinta:.1f}L')
        print(" ")
        print(f'Galões de Tinta: {latas_de_tinta:.0f} Galões.')
        print(f'Valor Total: R${valor_da_lata:.2f}')
    elif litros_de_tinta < 10:
        print(f'Litros de Tinta: {litros_de_tinta:.1f}L')
        print(f'Quantidade de litros de tinta não recomendavel para o uso de galões. prefira usar latas.')
        
elif escolha == "L":
    latas_de_tinta = litros_de_tinta / capacidade_latas
    valor_da_lata = 40 * latas_de_tinta
    print(f'Metros Quadrados: {metros_quadrados}m²')
    print(f'Litros de Tinta: {litros_de_tinta:.1f}L')
    print(" ")
    print(f'Latas de Tinta: {latas_de_tinta:.0f} Latas.')
    print(f'Valor Total: R${valor_da_lata:.2f}')
