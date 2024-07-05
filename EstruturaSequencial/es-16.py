largura = float(input("Largura: "))
altura = float(input("Altura: "))

metros_quadrados = largura * altura

capacidade_da_lata = 5
metros_por_litro = 3
valor_da_lata = 80

litros_de_tinta = metros_quadrados / metros_por_litro
latas_de_tinta = litros_de_tinta / capacidade_da_lata
valor_da_lata = 80 * latas_de_tinta


print(f'Area Total: {metros_quadrados}')
print(" ")
print(f'Litros de Tinta: {litros_de_tinta:.2f}L')
print(f'Latas de Tinta: {latas_de_tinta:.1f} Latas')
print(f'Valor da Lata: R${valor_da_lata:.2f}')

